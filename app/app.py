#!flask/bin/python
from flask import Flask, jsonify

from suggestions import generate_suggestions

app = Flask(__name__)


@app.route('/get-suggestions/<input_string>', methods=['GET'])
def get_suggestions(input_string):
    suggestions = generate_suggestions(input_string)
    return jsonify({'suggestions': suggestions})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)