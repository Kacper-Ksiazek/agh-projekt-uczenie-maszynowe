from flask import Flask, request, jsonify

app = Flask(__name__) # starts the app

# main page
@app.route('/')
def main_page():
    return 'Welcome to IAD LLM Model'

# healthcheck
@app.route('/healthcheck', methods=['POST'])
def healthcheck():
    if not request.is_json:
        return jsonify({'error': 'Request is not JSON'}), 400

    data = request.get_json()
    return jsonify(data)

