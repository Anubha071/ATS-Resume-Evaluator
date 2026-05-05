#  Load environment variables from .env file
import os
from dotenv import load_dotenv

load_dotenv()   # Load variables from .env file

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OPENAI_MODEL = os.getenv("OPENAI_MODEL")  # Default to gpt-3.5-turbo if not set.

GROQ_API_KEY = os.getenv("GROQ_API_KEY")   # Get Groq API key from environment variable.
GROQ_MODEL = os.getenv("GROQ_MODEL")  # Get Groq model from environment variable, which can be used for vector database operations and other tasks in the application.

# config acts as mediator for all configuration settings, so we can easily manage and access them across the application.