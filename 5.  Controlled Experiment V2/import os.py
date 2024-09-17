import os
import httpx
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Verify that the API key is available
if not api_key:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

# Set the OpenAI API endpoint
endpoint = "https://api.openai.com/v1/chat/completions"

# Set up the request headers with Bearer token for authentication
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Define the request payload
data = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Hello, how can I help you?"}]
}

# Send the request using httpx and log headers
with httpx.Client() as client:
    response = client.post(endpoint, headers=headers, json=data)

    # Log the request headers
    print("Request Headers:", response.request.headers)

    # Check the response status
    if response.status_code == 200:
        # Print the response from OpenAI
        print(response.json())
    else:
        print(f"Request failed with status code {response.status_code}: {response.text}")
