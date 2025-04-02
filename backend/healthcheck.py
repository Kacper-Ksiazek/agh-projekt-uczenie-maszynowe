from flask import Flask, request, jsonify
from model_gemini import *
app = Flask(__name__)

chat_session = model.start_chat(history=[])

@app.route('/generate', methods=['POST'])
def generate_response():
    data = request.get_json()
    if not data or "prompt" not in data:
        return jsonify({"error": "No prompt in request body"}), 400

    prompt = data["prompt"]

    try:
        response = model.generate_content(prompt)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


