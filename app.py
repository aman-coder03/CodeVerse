from flask import Flask, request, jsonify, render_template
from ai_engine import error_comedy_response
from voice_to_code import parse_voice_to_code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/voice-code', methods=['POST'])
def voice_code():
    data = request.json
    return jsonify({'code': parse_voice_to_code(data['voice'])})

@app.route('/error-response', methods=['POST'])
def error_response():
    data = request.json
    return jsonify({'response': error_comedy_response(data['error_type'])})

if __name__ == '__main__':
    app.run(debug=True)
