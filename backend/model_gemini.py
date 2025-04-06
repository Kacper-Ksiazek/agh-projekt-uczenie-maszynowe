import os
import google.generativeai as genai
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

# Create the model
generation_config = {
  "temperature": 0.95,
  "max_output_tokens": 8192,
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
    system_instruction ="""
    You are a dietitian tasked with creating a personalized meal plan for the user. 
    The plan should be based on the number of days provided by the user 
    and take into account all relevant parameters they provide, such as: 
    Age, Weight, Height, Gender, Goal, Activity Level, Cooking Time per Day, 
    Days, Allergies, Intolerances, Disliked Foods, Preferred Foods, Kitchen Equipment.\n\n

    Based on the user profile, create a balanced meal plan for the number of days specified. 
    Include breakfast, lunch, dinner, and snacks for each day, ensuring the plan is tailored to 
    the user's goal and preferences.\n\n

    Ensure the meals are suitable for the user's allergies, intolerances, and disliked foods. 
    Provide recipes or cooking methods that fit within the user's preferred cooking time and 
    available kitchen equipment.\n\n

    Make sure the meals align with the user's activity level and nutritional goals 
    (e.g., macronutrient distribution, total caloric intake, etc.).\n\n

    Offer alternative ingredients or meal ideas where necessary, particularly for foods the user 
    dislikes or is intolerant to. \n\n
    
    Budget is given in PLN.

    Everything you generate should be in Polish.\n\n
    """
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
    - Budget: {data.get("budget")} PLN

    - Allergies: { data.get("allergies", "None")}
    - Intolerances: { data.get("intolerance", "None")}
    - Disliked Foods: { data.get("disliked_foods", "None")}
    - Preferred Foods: { data.get("preferred_foods", "None")}
    - Kitchen Equipment: { data.get("kitchen_equipment" )}
    """

    expected_output = f"""
        Based on this profile, generate a {data.get("number_of_days")}-day diet plan with {data.get("number_of_meals")}-meals per day.

        Return only a valid JSON in this format:
        [
          [ 
              name: string;
              description: string;
              ingredients: string[];

              # I want macros to be for one portion, not for 100g
              macros: {{
                calories: number;
                protein: number;
                carbs: number;
                fat: number;
              }};

            recipe_in_steps: string[];
          ]
        ]

        It is 2D array, where the first dimension is the day, and the second dimension is the meal in that day.
        Meals for each day should be placed in order of their consumption.

        Do not include markdown, explanations, or formatting. Return only valid JSON without extra text suitable for JSON.parse().
        """  

    return user_info + "\n\n" + expected_output
