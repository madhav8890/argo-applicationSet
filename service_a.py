# service_a.py
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# State for service-a
state_a = {"data": []}

@app.route("/service-a", methods=["GET", "POST"])
def handle_service_a():
    if request.method == "POST":
        data = request.json
        state_a["data"].append(data)
        return jsonify({"message": "Data added to service-a", "state": state_a}), 201
    return jsonify({"message": "Service-A state", "state": state_a}), 200

@app.route("/service-a/call-service-b", methods=["POST"])
def call_service_b():
    data = request.json
    SERVICE_B_URL = os.getenv("SERVICE_B_URL", "http://service-b")  # Default to service-b's DNS name
    response = requests.post(f"{SERVICE_B_URL}/service-b", json=data)
    # response = requests.post("http://localhost:5001/service-b", json=data)
    return jsonify({"message": "Service-B called from Service-A", "response": response.json()}), response.status_code

if __name__ == "__main__":
    app.run(port=5000, debug=True)
