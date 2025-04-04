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
    generation_config=generation_config,
    system_instruction="You are just a cool guy. Talk to me like a gen z person"
)

# Create prompt to Gemini using user data
def data_to_prompt(data: dict) -> str:

    user_info = f"""The user profile:
- Age: {data.get("age")}
- Gender: {data.get("gender")}
- Weight: {data.get("current_weight")} kg
- Height: {data.get("height")} cm
- Exercises: {", ".join(data.get("exercise", []))}
- Schedule: {", ".join(data.get("schedule", []))}
- Allergies: {", ".join(data.get("allergies", []))}
- Intolerances: {", ".join(data.get("intolerances", []))}
- Diet type: {data.get("diet_type")}
- Disliked foods: {", ".join(data.get("disliked_foods", []))}
- Goal: {data.get("goal")}
- Weekly budget: {data.get("budget")} PLN
- Equipment: {", ".join(data.get("equipment", []))}
- Cooking time: {data.get("cooking_time")}
- Meal prep: {data.get("meal_prep")}
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
