

import requests

url = "http://127.0.0.1:5000/generate"

payload = {
    "age": 25,
    "gender": "male",
    "current_weight": 75,
    "height": 180,
    "exercise": ["gym", "cycling"],
    "schedule": ["morning", "evening"],
    "allergies": ["peanuts"],
    "intolerances": ["lactose"],
    "diet_type": "high protein",
    "disliked_foods": ["mushrooms"],
    "goal": "muscle gain",
    "budget": 200,
    "equipment": ["blender", "microwave"],
    "cooking_time": "30 minutes",
    "meal_prep": "yes"
}

response = requests.post(url, json=payload)

print("Status code:", response.status_code)
print("Response:")
print(response.json())
