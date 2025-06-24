from dotenv import load_dotenv
import os
from langchain.chat_models import init_chat_model

# Load environment variables from .env file
load_dotenv()

# Check if API key exists
if not os.environ.get("GOOGLE_API_KEY"):
    raise ValueError("GOOGLE_API_KEY not found in environment variables")

# Initialize the model
model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

# Use the model to get a response
response = model.invoke("What is LangChain used for?")
print(response)
