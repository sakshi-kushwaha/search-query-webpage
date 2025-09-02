#!/bin/bash

# Search Query Website - Automated Setup Script
# This script sets up both frontend and backend environments

set -e  # Exit on any error

echo "🚀 Setting up Search Query Website..."

# Check prerequisites
echo "📋 Checking prerequisites..."

if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed. Please install Python 3.8+"
    exit 1
fi

if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed. Please install Node.js 16+"
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo "❌ npm is required but not installed. Please install npm"
    exit 1
fi

echo "✅ Prerequisites check passed"

# Backend setup
echo "🐍 Setting up Python backend..."
cd backend

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file from template..."
    cp env.example .env
    echo "⚠️  Please edit backend/.env with your configuration"
else
    echo "✅ .env file already exists"
fi

echo "✅ Backend setup complete"

# Frontend setup
echo "⚛️  Setting up React frontend..."
cd ../frontend

# Install dependencies
echo "Installing Node.js dependencies..."
npm install

echo "✅ Frontend setup complete"

# Return to root directory
cd ..

echo ""
echo "🎉 Setup complete! Next steps:"
echo ""
echo "1. Edit backend/.env with your configuration"
echo "2. Start backend: cd backend && source venv/bin/activate && python manage.py runserver"
echo "3. Start frontend: cd frontend && npm start"
echo ""
echo "🌐 Frontend will be available at: http://localhost:3000"
echo "🔧 Backend API will be available at: http://localhost:8000"
echo ""
echo "Happy searching! 🔍✨" 