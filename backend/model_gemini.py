import os
import google.generativeai as genai
from dotenv import load_dotenv

from backend.orm import User_Allergies
from orm import SessionLocal, Users, Allergies
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import text

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

def save_user_data(data: dict) -> str:
    db = SessionLocal()

    try:
        user = Users(
            age=data.get("age"),
            height=data.get("height"),
            weight=data.get("weight"),
            gender=data.get("gender"),
            health_goal=data.get("goal"),
            exercise_frequency=data.get("activity_level"),
            meal_prep_time=data.get("cooking_time_per_day"),
            weekly_budget=data.get("budget"),
            disliked_foods=", ".join(map(str, data.get("disliked_foods", [])) if data.get("disliked_foods") else None)
        )
        db.add(user)
        db.execute(text("SELECT setval('allergies_id_seq', (SELECT MAX(id) FROM allergies))"))
        db.commit()
        db.refresh(user)
        allergy_names = data.get("allergies", [])

        for allergy_name in allergy_names:
            allergy = db.query(Allergies).filter_by(name=allergy_name).first()

            if not allergy:
                allergy = Allergies(name=allergy_name)
                db.add(allergy)
                db.commit()
                db.refresh(allergy)

            user_allergy = User_Allergies(user_id=user.id, allergy_id=allergy.id)
            db.add(user_allergy)



        return str(user.id)

    except SQLAlchemyError as e:
        print(f"[ERROR] Failed to save user data: {e}")
        db.rollback()
        return None

    finally:
        db.close()