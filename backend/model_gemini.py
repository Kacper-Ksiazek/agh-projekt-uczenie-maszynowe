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
    schedule_entries = []
    for s in data.get("schedule", []):
        entry = f"""    - Start: {s.get('start', '')}
    - End: {s.get('end', '')}
    - Description: {s.get('description', '')}"""
        schedule_entries.append(entry)

    schedule_str = "\n\n".join(schedule_entries) if schedule_entries else "None"

    user_info = f"""The user profile:
    - Age: {data.get("age")}
    - Height: {data.get("height")}
    - Weight: {data.get("weight")}
    - Gender: {data.get("gender")}
    - Goal: {data.get("goal")}  
    - Activity Level: {data.get("activity_level")}  
    - Cooking Time per Day: {data.get("cooking_time_per_day")}

    - Allergies: {", ".join(map(str, data.get("allergies", []))) or "None"}
    - Intolerances: {", ".join(map(str, data.get("intolerance", []))) or "None"}
    - Disliked Foods: {", ".join(map(str, data.get("disliked_foods", []))) or "None"}
    - Preferred Foods: {", ".join(map(str, data.get("preferred_foods", []))) or "None"}
    - Kitchen Equipment: {", ".join(map(str, data.get("kitchen_equipment", []))) or "None"}

    - Daily Schedule:
{schedule_str}
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
