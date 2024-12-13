# service_b.py
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# State for service-b
state_b = {"data": []}

@app.route("/service-b", methods=["GET", "POST"])
def handle_service_b():
    if request.method == "POST":
        data = request.json
        state_b["data"].append(data)
        return jsonify({"message": "Data added to service-b", "state": state_b}), 201
    return jsonify({"message": "Service-B state", "state": state_b}), 200

@app.route("/service-b/call-service-a", methods=["POST"])
def call_service_a():
    data = request.json
    SERVICE_A_URL = os.getenv("SERVICE_A_URL", "http://service-a")  # Default to service-a's DNS name
    response = requests.post(f"{SERVICE_A_URL}/service-a", json=data)
    # response = requests.post("http://localhost:5000/service-a", json=data)
    return jsonify({"message": "Service-A called from Service-B", "response": response.json()}), response.status_code

if __name__ == "__main__":
    app.run(port=5001, debug=True)
