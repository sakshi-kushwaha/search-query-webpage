# Demo Guide - Search Query Website

This guide will help you demonstrate the Search Query Website application effectively.

## 🚀 Quick Demo Setup

### 1. Start the Application

```bash
# Terminal 1: Start Backend
cd backend
source venv/bin/activate
python manage.py runserver

# Terminal 2: Start Frontend  
cd frontend
npm start
```

### 2. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000

## 🎯 Demo Scenarios

### Scenario 1: Wikipedia Search (Recommended for First Demo)

**URL**: `https://en.wikipedia.org/wiki/Sachin_Tendulkar`  
**Query**: `date of birth`

**Expected Results**:
- Title: "Sachin Ramesh Tendulkar... born 24 April 1973"
- High relevance score (90%+)
- Clean HTML content extraction
- Multiple relevant chunks

**Demo Points**:
- Show how the app processes complex Wikipedia pages
- Demonstrate content chunking and relevance scoring
- Highlight HTML structure preservation

### Scenario 2: Company Website Search

**URL**: `https://example.com` (or any company site)  
**Query**: `contact information`

**Expected Results**:
- Contact details, phone numbers, addresses
- Various content chunks with contact info
- Different relevance scores based on content quality

**Demo Points**:
- Show real-world website processing
- Demonstrate search across different content types
- Highlight the app's versatility

### Scenario 3: Blog/Article Search

**URL**: Any blog or news website  
**Query**: `machine learning` or `artificial intelligence`

**Expected Results**:
- Relevant articles and blog posts
- Content chunks with technical information
- Semantic understanding of search terms

**Demo Points**:
- Show content discovery capabilities
- Demonstrate search across articles
- Highlight intelligent content processing

## 🎨 Key Features to Highlight

### 1. **Smart Content Processing**
- "Notice how the app automatically removes navigation, ads, and scripts"
- "It preserves the meaningful content structure"
- "Content is intelligently chunked for better search"

### 2. **Advanced Search Algorithm**
- "The app doesn't just find exact matches"
- "It calculates relevance based on word frequency, content type, and quality"
- "Headings and important content get bonus points"

### 3. **Rich Results Display**
- "Each result shows a title, path, and match percentage"
- "You can expand to see the actual HTML structure"
- "Results are color-coded by relevance"

### 4. **User Experience**
- "Clean, modern interface that's easy to use"
- "Loading states and error handling"
- "Responsive design that works on all devices"

## 🔧 Technical Demo Points

### Backend Capabilities
- **HTML Parsing**: BeautifulSoup4 processing
- **Content Extraction**: Intelligent element filtering
- **Search Algorithm**: Relevance scoring system
- **API Design**: RESTful endpoints

### Frontend Features
- **React Components**: Modular architecture
- **State Management**: Efficient data handling
- **CSS Styling**: Modern, responsive design
- **Error Handling**: User-friendly error messages

## 🚨 Troubleshooting During Demo

### Common Issues & Solutions

1. **"No results found"**
   - Check if the URL is accessible
   - Verify the search query has meaningful words
   - Try a different website or query

2. **Slow loading**
   - Large websites may take time to process
   - Explain that this is normal for complex pages
   - Show the loading animation

3. **CORS errors**
   - Ensure backend is running on port 8000
   - Check browser console for errors
   - Verify CORS settings

4. **Empty results**
   - Some websites may block scraping
   - Try websites that allow public access
   - Use Wikipedia or news sites for reliable demos

## 💡 Demo Tips

### Before the Demo
- Test all scenarios beforehand
- Have backup URLs ready
- Ensure both services are running smoothly
- Clear browser cache if needed

### During the Demo
- Start with the Wikipedia example (most reliable)
- Explain each step as you go
- Show the HTML expansion feature
- Demonstrate different search queries
- Highlight the relevance scoring

### After the Demo
- Show the code structure briefly
- Explain the technology stack
- Discuss potential use cases
- Answer questions about implementation

## 🎯 Demo Script Example

```
"Let me show you how this Search Query Website works. 

First, I'll enter a Wikipedia URL and search for 'date of birth'...

[Enter URL and query]

Notice how the app processes the page and extracts relevant content chunks. 
It automatically removes navigation and ads, keeping only the meaningful content.

[Show results]

Here we can see the top results with relevance scores. The highest match 
shows Sachin Tendulkar was born on April 24, 1973. Each result includes 
a title, path, and match percentage.

[Expand HTML view]

You can also view the actual HTML structure for each result, which is 
useful for developers who want to understand the content structure.

[Try another example]

Let me show you how it works with a different type of website..."
```

## 🚀 Next Steps After Demo

1. **Answer Questions**: Be prepared for technical questions
2. **Show Code**: Briefly highlight key implementation details
3. **Discuss Use Cases**: Talk about potential applications
4. **Future Plans**: Mention planned enhancements
5. **Get Feedback**: Ask for suggestions and improvements

---

**Remember**: The goal is to demonstrate a working, professional application that solves real problems. Focus on the user experience and practical value rather than just technical implementation. 