from flask import Flask, request, jsonify
from flask_cors import CORS
from enum import Enum
import os
from dotenv import load_dotenv
dotenv_path = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path)

app = Flask(__name__)
cors = CORS(app)

class Calulator(Enum):
    addition = "+"
    subtraction = "-"
    multiplication = "*"


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response

@app.route("/math", methods=["POST"])
def calculate():
    result = 0
    body = request.get_json()
    operation_type = body.get("operation_type")
    x = body["x"]
    y = body.get("y")
    
    if "subtraction" in operation_type:
        result = x - y
        Calulator.value = "substraction"

    elif "addition" in operation_type:
        result = x + y
        Calulator.value = "addition"

    elif "multiplication" in operation_type:
        result = x * y
        Calulator.value = "multiplication"


    return jsonify({
        "slackUsername": "Nimi",
        "result": result,
        "operation_type": Calulator.value
    }), 200, {"content-type": "application/json"}



if __name__ == "__main__":
    app.run(debug=True)
    port = int(os.environ.get('PORT', 33507))









    # or "subtract" or "minus" or "difference"
    # , "multiply", "times", "mul"
    #  or "add" or "join" 
    # integers = [x for x in operation_type.isdigit()]
    # if integers in operation_type:
    #     opt_x = int(integers[0])
    #     opt_y = int(integers[1])
    
    #     if opt_x == x and opt_y == y :
    #         continue
    # else:
