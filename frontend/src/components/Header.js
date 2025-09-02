import React from 'react';
import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="header-content">
        <h1 className="header-title">
          <span className="search-icon">🔍</span>
          Search Query Website
        </h1>
        <p className="header-subtitle">
          Extract and search relevant content from any website
        </p>
      </div>
    </header>
  );
};

export default Header; 