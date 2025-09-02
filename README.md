# Search Query Website

A single-page application (SPA) that allows users to input a website URL and search query to find the most relevant HTML content chunks using intelligent search algorithms.

## 🚀 Features

- **Frontend**: React-based SPA with modern, responsive UI/UX
- **Backend**: Django REST API for web scraping and content processing
- **HTML Processing**: BeautifulSoup4 for parsing and cleaning HTML content
- **Intelligent Chunking**: Content split into meaningful chunks (max 500 tokens)
- **Advanced Search**: Keyword-based search with relevance scoring
- **Rich Results**: Display titles, paths, match percentages, and expandable HTML content
- **Modern Design**: Clean interface with loading states and error handling

## 🏗️ Project Structure

```
search-query-website/
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/      # React components (Header, SearchForm, SearchResults)
│   │   ├── App.js          # Main application component
│   │   └── index.js        # Application entry point
│   ├── public/              # Static assets
│   ├── package.json         # Node.js dependencies
│   └── Dockerfile          # Frontend container configuration
├── backend/                  # Django backend application
│   ├── search_app/          # Main Django app with search logic
│   ├── search_project/      # Django project settings
│   ├── requirements.txt     # Python dependencies
│   ├── manage.py           # Django management script
│   ├── env.example         # Environment variables template
│   └── Dockerfile          # Backend container configuration
├── README.md                # This comprehensive documentation
├── docker-compose.yml       # Docker setup for easy deployment
└── setup.sh                # Automated setup script
```

## 📋 Prerequisites

- **Python 3.8+** with pip
- **Node.js 16+** with npm
- **Git** for version control
- **Docker** (optional, for containerized deployment)

## 🛠️ Quick Setup

### Option 1: Automated Setup (Recommended)

```bash
# Clone the repository
git clone <repository-url>
cd search-query-website

# Run the automated setup script
chmod +x setup.sh
./setup.sh
```

### Option 2: Manual Setup

#### Backend Setup

```bash
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set environment variables
cp env.example .env
# Edit .env with your configuration

# Run Django
python manage.py migrate
python manage.py runserver
```

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the `backend/` directory:

```bash
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Pinecone Configuration (for future semantic search)
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_ENVIRONMENT=your-pinecone-environment
PINECONE_INDEX_NAME=your-index-name
```

### API Endpoints

- `POST /api/search/` - Submit URL and search query
- `GET /api/health/` - Health check endpoint

## 🎯 How It Works

### 1. **Content Fetching**
- Fetches HTML content from the provided URL
- Uses proper User-Agent headers for compatibility

### 2. **HTML Processing**
- BeautifulSoup4 parses and cleans HTML content
- Removes scripts, styles, navigation, and other non-content elements
- Preserves meaningful content structure

### 3. **Content Chunking**
- Splits content into semantic chunks (max 500 tokens)
- Maintains HTML structure for context
- Creates meaningful boundaries between chunks

### 4. **Intelligent Search**
- Performs keyword-based search across chunks
- Calculates relevance scores based on:
  - Word frequency and density
  - Exact phrase matches
  - Element type (headings get bonus points)
  - Content length and quality

### 5. **Result Ranking**
- Sorts results by relevance score
- Returns top 10 most relevant matches
- Displays match percentages with color coding

## 🎨 User Interface

### Search Form
- Clean input fields for URL and search query
- Form validation and error handling
- Loading states during processing

### Results Display
- **Title**: Extracted from content (first sentence or first 100 characters)
- **Path**: Simplified HTML element path
- **Match Percentage**: Color-coded relevance score
- **Content Preview**: Clean text excerpt
- **HTML View**: Expandable HTML structure display
- **Word Count**: Content length indicator

## 🚀 Usage Examples

### Example 1: Wikipedia Search
```
URL: https://en.wikipedia.org/wiki/Sachin_Tendulkar
Query: date of birth
```
**Result**: "Sachin Ramesh Tendulkar... born 24 April 1973"

### Example 2: Company Website Search
```
URL: https://example.com
Query: contact information
```
**Result**: Contact details, phone numbers, email addresses

### Example 3: Blog Search
```
URL: https://blog.example.com
Query: machine learning
```
**Result**: Relevant blog posts and articles about ML

## 🛠️ Development

### Running Tests

```bash
# Backend tests
cd backend
python manage.py test

# Frontend tests
cd frontend
npm test
```

### Code Quality

```bash
# Backend
cd backend
flake8 .
black .

# Frontend
cd frontend
npm run lint
npm run format
```

## 🐳 Docker Deployment

### Quick Start with Docker

```bash
# Build and run with Docker Compose
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Manual Docker Build

```bash
# Backend
cd backend
docker build -t search-backend .
docker run -p 8000:8000 search-backend

# Frontend
cd frontend
docker build -t search-frontend .
docker run -p 3000:3000 search-frontend
```

## 🔧 Troubleshooting

### Common Issues

1. **Frontend won't compile**
   - Ensure Node.js version is 16+
   - Clear node_modules and reinstall: `rm -rf node_modules && npm install`

2. **Backend won't start**
   - Check Python version (3.8+)
   - Verify virtual environment is activated
   - Check all dependencies are installed

3. **Search returns no results**
   - Verify the URL is accessible
   - Check if the website requires JavaScript
   - Ensure the search query has meaningful words

4. **CORS errors**
   - Verify backend is running on port 8000
   - Check CORS settings in Django settings

### Debug Mode

Enable debug logging in the backend:

```python
# In backend/search_project/settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}
```

## 🚀 Future Enhancements

### Planned Features
- **Semantic Search**: Integration with Pinecone vector database
- **Advanced NLP**: Better content understanding and chunking
- **Caching**: Redis-based result caching
- **User Accounts**: Save search history and favorites
- **API Rate Limiting**: Protect against abuse
- **Content Filtering**: Safe search and content moderation

### Technical Improvements
- **Performance**: Async processing for large websites
- **Scalability**: Microservices architecture
- **Monitoring**: Application performance monitoring
- **Testing**: Comprehensive test coverage
- **CI/CD**: Automated deployment pipeline

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 for Python code
- Use ESLint for JavaScript/React code
- Write meaningful commit messages
- Add tests for new features
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **BeautifulSoup4** for HTML parsing
- **Django** for the robust backend framework
- **React** for the modern frontend framework
- **Docker** for containerization
- **Open Source Community** for inspiration and tools

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Search existing issues in the repository
3. Create a new issue with detailed information
4. Include error messages, logs, and reproduction steps

---

**Happy Searching! 🔍✨**