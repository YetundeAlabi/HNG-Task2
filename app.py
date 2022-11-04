from flask import Flask, request, jsonify
from flask_cors import CORS
from enum import Enum
import os
from dotenv import load_dotenv
dotenv_path = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path)

app = Flask(__name__)
cors = CORS(app)

class Operator(Enum):
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

    
    if any(x in operation_type for x in ["subtraction", "subtract", "minus", "difference"]):  # checking if any of the string occurs in operation type
        result = x - y
        Operator.value = "subtraction"

    elif any(x in operation_type for x in ["addition", "add", "plus", "join"]):
        result = x + y
        Operator.value = "addition"

    elif any(x in operation_type for x in ["multiplication" , "times", "multiply"]):
        result = x * y
        Operator.value = "multiplication"


    return jsonify({
        "slackUsername": "Nimi",
        "result": result,
        "operation_type": Operator.value
    }), 200, {"content-type": "application/json"}



if __name__ == "__main__":
    app.run(debug=True)
    port = int(os.environ.get('PORT', 33507))

