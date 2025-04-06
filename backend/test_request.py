

import requests

url = "http://127.0.0.1:5000/generate"

payload = {
    "age": 25,
    "gender": "male",
    "weight": 75,
    "height": 180,
    "activity_level": " 5 times per week",
    "schedule": ["morning", "evening"],
    "allergies": ["peanuts", "milk", "dairy", "celery"],
    "intolerances": ["lactose"],
    "diet_type": "high protein",
    "disliked_foods": ["mushrooms"],
    "goal": "muscle gain",
    "budget": 200,
    "equipment": ["blender", "microwave"],
    "cooking_time_per_day": "30 minutes",
    "meal_prep": "yes"
}

response = requests.post(url, json=payload)

print("Status code:", response.status_code)
print("Response:")
print(response.json())
