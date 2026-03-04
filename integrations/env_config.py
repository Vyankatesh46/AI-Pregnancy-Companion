"""
Environment Configuration Management
Person 5: Voice + Integrations + DevOps
"""

from dotenv import load_dotenv
import os
from typing import Dict


def load_environment() -> Dict[str, str]:
    """
    Load environment variables from .env file
    
    Returns:
        Dictionary with required environment variables
    
    Raises:
        KeyError: If OPENAI_API_KEY is missing
    """
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise KeyError(
            "OPENAI_API_KEY not found in environment variables. "
            "Please set it in .env file."
        )
    
    return {
        "OPENAI_API_KEY": api_key
    }


def validate_environment() -> bool:
    """
    Validate all required environment variables are set
    
    Returns:
        True if all variables are valid
    
    Raises:
        EnvironmentError: If critical variables are missing
    """
    try:
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        
        if not api_key:
            raise EnvironmentError(
                "OPENAI_API_KEY is not set. "
                "Check your .env file configuration."
            )
        
        return True
    except Exception as e:
        raise EnvironmentError(f"Environment validation failed: {str(e)}")
