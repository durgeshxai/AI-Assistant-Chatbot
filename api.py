from flask import Flask, request, jsonify, send_from_directory
from Chat import get_response

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'Index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message')
    if not message:
        return jsonify({'error': 'No message provided'}), 400

    response = get_response(message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Using port 5001 to avoid potential conflicts