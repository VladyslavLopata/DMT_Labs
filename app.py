import lab1.math_manager as maths
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/api/lab1', methods=['POST'])
def lab1():
    return jsonify(maths.solve(request.json))
