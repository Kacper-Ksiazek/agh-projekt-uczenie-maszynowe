from flask import Flask, request, jsonify
from model_gemini import *
from model_gemini import data_to_prompt

app = Flask(__name__)

chat_session = model.start_chat(history=[])

@app.route('/generate', methods=['POST'])
def generate_response():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data in request body"}), 400

    prompt = data_to_prompt(data)
    user_id = save_user_data(data)
    if not user_id:
        return jsonify({"error": "Failed to save user data"}), 500
    import json
    try:
        response = model.generate_content(prompt)
        parsed = json.loads(response.text)
        return jsonify({"response": parsed})
    except json.JSONDecodeError:
        return jsonify({"response_raw": response.text, "note": "Gemini did not return valid JSON"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



