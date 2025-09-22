"""Configuration settings for QueryLens."""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration."""
    
    GROQ_API_KEY = os.getenv('GROQ_API_KEY')
    TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
    
    DATABASE_PATH = os.getenv('DATABASE_PATH', 'reports.db')
    
    MAX_SEARCH_RESULTS = int(os.getenv('MAX_SEARCH_RESULTS', '3'))
    SEARCH_DEPTH = os.getenv('SEARCH_DEPTH', 'advanced')
    
    # LLM Settings
    LLM_MODEL = os.getenv('LLM_MODEL', 'llama-3.1-8b-instant')
    MAX_TOKENS = int(os.getenv('MAX_TOKENS', '1500'))
    TEMPERATURE = float(os.getenv('TEMPERATURE', '0.3'))
    
    # Content Extraction
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', '2000'))
    REQUEST_TIMEOUT = int(os.getenv('REQUEST_TIMEOUT', '10'))
    
    @classmethod
    def validate(cls):
        """Validate required configuration."""
        if not cls.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is required")
        if not cls.TAVILY_API_KEY:
            raise ValueError("TAVILY_API_KEY is required")
        return True
