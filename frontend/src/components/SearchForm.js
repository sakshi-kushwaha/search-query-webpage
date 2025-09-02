import React, { useState } from 'react';
import './SearchForm.css';

const SearchForm = ({ onSearch, isLoading }) => {
  const [url, setUrl] = useState('');
  const [query, setQuery] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (url.trim() && query.trim()) {
      onSearch(url.trim(), query.trim());
    }
  };

  const isValidUrl = (url) => {
    try {
      new URL(url);
      return true;
    } catch {
      return false;
    }
  };

  return (
    <div className="search-form-container">
      <form className="search-form" onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="url" className="form-label">
            Website URL
          </label>
          <input
            type="url"
            id="url"
            className={`form-input ${url && !isValidUrl(url) ? 'error' : ''}`}
            placeholder="https://example.com"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            required
            disabled={isLoading}
          />
          {url && !isValidUrl(url) && (
            <span className="error-text">Please enter a valid URL</span>
          )}
        </div>

        <div className="form-group">
          <label htmlFor="query" className="form-label">
            Search Query
          </label>
          <input
            type="text"
            id="query"
            className="form-input"
            placeholder="Enter your search query..."
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            required
            disabled={isLoading}
          />
        </div>

        <button
          type="submit"
          className={`search-button ${isLoading ? 'loading' : ''}`}
          disabled={isLoading || !url.trim() || !query.trim() || !isValidUrl(url)}
        >
          {isLoading ? (
            <>
              <span className="spinner"></span>
              Searching...
            </>
          ) : (
            'Search'
          )}
        </button>
      </form>
    </div>
  );
};

export default SearchForm; 