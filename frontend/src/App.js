import React, { useState } from 'react';
import './App.css';
import SearchForm from './components/SearchForm';
import SearchResults from './components/SearchResults';
import Header from './components/Header';

function App() {
  const [searchResults, setSearchResults] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async (url, query) => {
    setIsLoading(true);
    setError(null);
    
    try {
      const response = await fetch('/api/search/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url, query }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || 'Search failed');
      }

      setSearchResults(data.results || []);
    } catch (err) {
      setError(err.message);
      setSearchResults([]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <Header />
      <main className="main-content">
        <SearchForm onSearch={handleSearch} isLoading={isLoading} />
        {error && (
          <div className="error-message">
            <p>Error: {error}</p>
          </div>
        )}
        <SearchResults 
          results={searchResults} 
          isLoading={isLoading}
          totalResults={searchResults.length}
        />
      </main>
    </div>
  );
}

export default App; 