import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=API_KEY)

# Create the model
generation_config = {
  "temperature": 0.25,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction="You are just a cool guy. Talk to me like a gen z person"
)

