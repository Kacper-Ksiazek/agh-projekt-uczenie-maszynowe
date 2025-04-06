import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

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
    generation_config=generation_config
)

# Create prompt to Gemini using user data
def data_to_prompt(data: dict) -> str:
    user_info = f"""The user profile:
    - Age: {data.get("age")}
    - Height: {data.get("height")}
    - Weight: {data.get("weight")}
    - Gender: {data.get("gender")}
    - Goal: {data.get("goal")}  
    - Activity Level: {data.get("activity_level")}  
    - Cooking Time per Day: {data.get("cooking_time_per_day")}

    - Allergies: {", ".join(data.get("allergies"))}
    - Intolerances: {", ".join(data.get("intolerance"))}
    - Disliked Foods: {", ".join(data.get("disliked_foods"))}
    - Preferred Foods: {", ".join(data.get("preferred_foods"))}
    - Kitchen Equipment: {", ".join(data.get("kitchen_equipment"))}

    - Daily Schedule:
      - Start: {data.get("schedule", {}).get("start")}
      - End: {data.get("schedule", {}).get("end")}
      - Description: {data.get("schedule", {}).get("description")}
    """

    expected_output = """
    Based on this profile, generate a 7-day diet plan.

    Return only a valid JSON in this format:
    {
    
    
      "days": [
        {
          "day": "Monday",
          "meals": [
            {
              "name": "Meal Name",
              "ingredients": ["ingredient1", "ingredient2"],
              "instructions": "How to prepare"
            }
          ]
        }
      ]
    }

    Do not include markdown, explanations, or formatting. Return only valid JSON without extra text.
    """
    return user_info + "\n\n" + expected_output
