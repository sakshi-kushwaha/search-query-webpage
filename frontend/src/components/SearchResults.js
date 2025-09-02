import React, { useState } from 'react';
import './SearchResults.css';

const SearchResults = ({ results, isLoading, totalResults }) => {
  const [expandedHtml, setExpandedHtml] = useState({});

  const toggleHtml = (id) => {
    setExpandedHtml(prev => ({
      ...prev,
      [id]: !prev[id]
    }));
  };

  if (isLoading) {
    return (
      <div className="search-results-container">
        <div className="loading-container">
          <div className="loading-spinner"></div>
          <p>Processing your search request...</p>
          <p className="loading-details">
            This may take a few moments as we analyze the website content
          </p>
        </div>
      </div>
    );
  }

  if (results.length === 0) {
    return (
      <div className="search-results-container">
        <div className="no-results">
          <p>No results to display yet.</p>
          <p>Enter a website URL and search query to get started.</p>
        </div>
      </div>
    );
  }

  return (
    <div className="search-results-container">
      <div className="results-header">
        <h2>Search Results</h2>
        <p className="results-count">
          Found {totalResults} relevant content chunks
        </p>
      </div>

      <div className="results-list">
        {results.map((result) => (
          <div key={result.id} className="result-item">
            <div className="result-header">
              <div className="result-title">
                <h3>{result.title}</h3>
                <span className="result-path">{result.path}</span>
              </div>
              <div className="result-meta">
                <span className={`match-percentage ${result.match_percentage >= 80 ? 'high' : result.match_percentage >= 60 ? 'medium' : 'low'}`}>
                  {result.match_percentage}% match
                </span>
                <span className="word-count">
                  {result.word_count} words
                </span>
              </div>
            </div>
            
            <div className="result-content">
              <p>{result.content}</p>
            </div>
            
            <div className="result-actions">
              <button
                className="view-html-btn"
                onClick={() => toggleHtml(result.id)}
              >
                {expandedHtml[result.id] ? 'Hide HTML' : 'View HTML'}
              </button>
            </div>
            
            {expandedHtml[result.id] && (
              <div className="html-content">
                <pre><code>{result.html_content}</code></pre>
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  );
};

export default SearchResults; 