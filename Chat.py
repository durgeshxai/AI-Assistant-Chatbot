import os
import google.generativeai as genai

# IMPORTANT:
# 1. Get your API key from Google AI Studio: https://aistudio.google.com/app/apikey
# 2. Set it as an environment variable named "GEMINI_API_KEY"
#    For Windows: setx GEMINI_API_KEY "YOUR_API_KEY"
#    For macOS/Linux: export GEMINI_API_KEY="YOUR_API_KEY"
# 3. Alternatively, you can uncomment the line below and paste your key directly.
#    genai.configure(api_key="YOUR_API_KEY")

chat = None

try:
    # The API key is now hardcoded below.
    genai.configure(api_key="AIzaSyC4pGJfTxy9FEWj65vZ13EfUm4yBgwJhhU")
    model = genai.GenerativeModel('gemini-2.5 flash-lite')
    chat = model.start_chat(history=[])
    print("Chat session initialized successfully.")
except Exception as e:
    print(f"An unexpected error occurred during initialization: {e}")

def get_response(message: str) -> str:
    """
    Generates a response using the Gemini API and maintains conversation history.
    """
    if chat is None:
        return 'Error: Chat session is not initialized. Please check the server logs.'

    try:
        response = chat.send_message(message)
        return response.text
    except Exception as e:
        return f"An error occurred while generating a response: {e}"