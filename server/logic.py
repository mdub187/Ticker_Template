import os
import sys
import flask
from flask import request, jsonify
rootdir = os.path.dirname(os.path.abspath("./"))
from client import gui
app = flask.Flask(__name__)
import api.routes
# @app.route('/api/score', methods=['POST'])
def update_score():
    data = request.get_json()
    # update logic here
    score = data.get('score', 0)
    return jsonify({'status': 'success'})

# @app.route('/api/score', methods=['GET'])
def get_score():
    # Retrieve the score logic here
    return jsonify({'score': 0})

# @app.route('/api/score', methods=['PUT'])
def reset_score():
    # Reset the score logic here
    return jsonify({'status': 'success'})

print("Great Success", app)

if __name__ == '__main__':
    print(__name__)
