import lab1.math_manager as maths
from flask import Flask, jsonify, request
from flask_cors import CORS
from lab3.math_solver import solve

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/lab1', methods=['POST'])
def lab1():
    return jsonify(maths.solve(request.json))

@app.route('/api/lab3', methods=['POST'])
def lab2():
    return jsonify(solve(request.json))