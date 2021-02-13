'''
Main Flask app.
Used for routing.
'''

from flask import Flask, jsonify, request
from flask_cors import CORS

import lab1.math_manager as l1
import lab2.solver as l2
import lab3.math_solver as l3

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


@app.route('/api/lab1', methods=['POST'])
def lab1():
    '''
    LAB 1:
    Метод безпосередньої оцінки порівняльної переваги альтернатив.
    '''
    return jsonify(l1.solve(request.json))


@app.route('/api/lab2', methods=['POST'])
def lab2():
    '''
    LAB 2:
    Критерії прийняття рішень в умовах невизначеності.
    '''
    return jsonify(l2.solve(request.json))


@app.route('/api/lab3', methods=['POST'])
def lab3():
    '''
    LAB 3:
    Критерії Севіджа і Лапласа.
    '''
    return jsonify(l3.solve(request.json))
