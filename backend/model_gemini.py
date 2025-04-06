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
    system_instruction =
    "You are a dietitian tasked with creating a personalized meal plan for the user. "
    "The plan should be based on the number of days provided by the user "
    "and take into account all relevant parameters they provide, such as: "
    "Age, Weight, Height, Gender, Goal, Activity Level, Cooking Time per Day, "
    "Days, Allergies, Intolerances, Disliked Foods, Preferred Foods, Kitchen Equipment.\n\n"

    "Based on the user profile, create a balanced meal plan for the number of days specified. "
    "Include breakfast, lunch, dinner, and snacks for each day, ensuring the plan is tailored to "
    "the user's goal and preferences.\n\n"

    "Ensure the meals are suitable for the user's allergies, intolerances, and disliked foods. "
    "Provide recipes or cooking methods that fit within the user's preferred cooking time and "
    "available kitchen equipment.\n\n"

    "Make sure the meals align with the user's activity level and nutritional goals "
    "(e.g., macronutrient distribution, total caloric intake, etc.).\n\n"

    "Offer alternative ingredients or meal ideas where necessary, particularly for foods the user "
    "dislikes or is intolerant to. \n\n"
    
    "Budget is given in PLN."
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
    - Days: {data.get("number_of_days")}
    - Budget: {data.get("budget")} PLN

    - Allergies: {", ".join(map(str, data.get("allergies", []))) or "None"}
    - Intolerances: {", ".join(map(str, data.get("intolerance", []))) or "None"}
    - Disliked Foods: {", ".join(map(str, data.get("disliked_foods", []))) or "None"}
    - Preferred Foods: {", ".join(map(str, data.get("preferred_foods", []))) or "None"}
    - Kitchen Equipment: {", ".join(map(str, data.get("kitchen_equipment", []))) or "None"}

    """

    expected_output = """
        Based on this profile, generate a {days}-day diet plan.

        Return only a valid JSON in this format:
        {{
          "days": [
            {{
              "day": "Monday",
              "meals": [
                {{
                  "name": "Meal Name",
                  "ingredients": ["ingredient1", "ingredient2"],
                  "macros": ["calories", "protein", "carbs", "fat"],
                  "recipe_in_steps": ["step1", "step2", "step3"]
                }}
              ]
            }}
          ]
        }}

        Do not include markdown, explanations, or formatting. Return only valid JSON without extra text.
        """.format(days=data.get("days", 7))  # Domyślnie 7 dni jeśli nie podano
    return user_info + "\n\n" + expected_output
