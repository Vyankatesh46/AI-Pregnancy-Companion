import os
from dotenv import load_dotenv


def load_environment():
    """
    Load environment variables from .env file
    """
    load_dotenv()
    return True


def validate_environment():
    """
    Validate required environment variables
    """
    load_dotenv()

    required_vars = ["OPENAI_API_KEY"]

    missing = []

    for var in required_vars:
        if not os.getenv(var):
            missing.append(var)

    if missing:
        raise Exception(f"Missing environment variables: {missing}")

    return True