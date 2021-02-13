import lab1.math_manager as maths
import lab2.solver as solver
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/lab1', methods=['POST'])
def lab1():
    return jsonify(maths.solve(request.json))

@app.route('/api/lab2', methods=['POST'])
def lab2():
    return jsonify(solver.Solve(request.json))
