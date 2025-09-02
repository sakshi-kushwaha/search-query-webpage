import logging
import re
from typing import List, Dict, Any
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

logger = logging.getLogger(__name__)


class HealthCheckView(View):
    """Health check endpoint."""
    
    def get(self, request):
        return JsonResponse({'status': 'healthy', 'message': 'Search API is running'})


@method_decorator(csrf_exempt, name='dispatch')
class SearchView(View):
    """Enhanced search view for processing URLs and queries with HTML content preservation."""
    
    def post(self, request):
        """Handle POST request for search functionality."""
        try:
            # Parse request data
            data = request.POST if request.POST else request.body
            if hasattr(data, 'decode'):
                import json
                data = json.loads(data.decode('utf-8'))
            
            url = data.get('url', '').strip()
            query = data.get('query', '').strip()
            
            # Validate inputs
            if not url or not query:
                return JsonResponse({
                    'error': 'Both URL and query are required'
                }, status=400)
            
            if not self._is_valid_url(url):
                return JsonResponse({
                    'error': 'Invalid URL format'
                }, status=400)
            
            # Process the search
            results = self._process_search(url, query)
            
            return JsonResponse({
                'success': True,
                'results': results,
                'total_chunks': len(results)
            })
            
        except Exception as e:
            logger.error(f"Error in search view: {e}")
            return JsonResponse({
                'error': 'Internal server error',
                'details': str(e)
            }, status=500)
    
    def _is_valid_url(self, url: str) -> bool:
        """Validate URL format."""
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False
    
    def _fetch_html_content(self, url: str) -> str:
        """Fetch HTML content from the given URL."""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            return response.text
        except Exception as e:
            logger.error(f"Error fetching HTML from {url}: {e}")
            raise
    
    def _extract_content_chunks(self, html_content: str, max_tokens: int = 500) -> List[Dict[str, Any]]:
        """Extract meaningful content chunks with HTML structure preserved."""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Remove unwanted elements
            for element in soup(["script", "style", "nav", "footer", "header", "aside"]):
                element.decompose()
            
            chunks = []
            chunk_id = 0
            
            # Extract content from different types of elements
            content_elements = soup.find_all(['div', 'section', 'article', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
            
            for element in content_elements:
                # Skip empty or very short elements
                if not element.get_text(strip=True) or len(element.get_text(strip=True)) < 10:
                    continue
                
                # Get text content
                text_content = element.get_text(strip=True)
                words = text_content.split()
                
                # Skip if too short
                if len(words) < 5:
                    continue
                
                # Create chunk
                chunk = {
                    'id': chunk_id,
                    'content': text_content,
                    'html_content': str(element),
                    'element_type': element.name,
                    'word_count': len(words),
                    'token_count': len(words),  # Simple word-based tokenization
                    'path': self._get_element_path(element),
                    'relevance_score': 0.0
                }
                
                chunks.append(chunk)
                chunk_id += 1
                
                # Limit total chunks to avoid overwhelming results
                if chunk_id >= 50:
                    break
            
            return chunks
            
        except Exception as e:
            logger.error(f"Error extracting content chunks: {e}")
            raise
    
    def _get_element_path(self, element) -> str:
        """Get a simplified path representation for the element."""
        try:
            path_parts = []
            current = element
            
            while current and current.name != 'body':
                if current.name:
                    path_parts.append(current.name)
                current = current.parent
            
            if path_parts:
                return '/' + '/'.join(reversed(path_parts))
            return '/content'
        except:
            return '/content'
    
    def _search_chunks(self, chunks: List[Dict[str, Any]], query: str) -> List[Dict[str, Any]]:
        """Enhanced search with better relevance scoring."""
        try:
            query_words = [word.lower() for word in query.split() if len(word) > 2]
            results = []
            
            for chunk in chunks:
                chunk_text = chunk['content'].lower()
                score = 0.0
                
                # Calculate relevance score
                for word in query_words:
                    if word in chunk_text:
                        # Count occurrences
                        occurrences = chunk_text.count(word)
                        # Normalize by chunk length
                        word_density = occurrences / len(chunk['content'].split())
                        score += word_density * 2  # Boost word matches
                        
                        # Bonus for exact phrase matches
                        if query.lower() in chunk_text:
                            score += 0.5
                
                # Bonus for title/heading elements
                if chunk['element_type'] in ['h1', 'h2', 'h3']:
                    score += 0.3
                
                # Bonus for longer, more substantial content
                if chunk['word_count'] > 20:
                    score += 0.1
                
                if score > 0:
                    chunk['relevance_score'] = min(score, 1.0)
                    results.append(chunk)
            
            # Sort by relevance score (highest first)
            results.sort(key=lambda x: x['relevance_score'], reverse=True)
            
            return results
            
        except Exception as e:
            logger.error(f"Error in search: {e}")
            raise
    
    def _process_search(self, url: str, query: str) -> List[Dict[str, Any]]:
        """Main method to process the search request."""
        try:
            # Step 1: Fetch HTML content
            logger.info(f"Fetching HTML content from: {url}")
            html_content = self._fetch_html_content(url)
            
            # Step 2: Extract content chunks with HTML structure
            logger.info("Extracting content chunks")
            chunks = self._extract_content_chunks(html_content)
            logger.info(f"Created {len(chunks)} chunks")
            
            # Step 3: Search chunks
            logger.info("Searching chunks")
            results = self._search_chunks(chunks, query)
            
            # Step 4: Format results for frontend
            formatted_results = []
            for i, result in enumerate(results[:10]):  # Top 10 results
                formatted_result = {
                    'id': result['id'],
                    'title': self._extract_title(result['content']),
                    'content': result['content'],
                    'html_content': result['html_content'],
                    'path': result['path'],
                    'relevance_score': result['relevance_score'],
                    'match_percentage': int(result['relevance_score'] * 100),
                    'word_count': result['word_count'],
                    'element_type': result['element_type']
                }
                formatted_results.append(formatted_result)
            
            return formatted_results
            
        except Exception as e:
            logger.error(f"Error processing search: {e}")
            raise
    
    def _extract_title(self, content: str) -> str:
        """Extract a title from content."""
        try:
            # Take first sentence or first 100 characters
            sentences = content.split('.')
            if sentences and sentences[0]:
                title = sentences[0].strip()
                if len(title) > 100:
                    title = title[:100] + '...'
                return title
            else:
                return content[:100] + '...' if len(content) > 100 else content
        except:
            return content[:100] + '...' if len(content) > 100 else content 