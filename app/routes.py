from flask import Flask, request, jsonify
from app.analyzer import analyze_requirements
from app.risk_predictor import predict_risk

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    """Endpoint to analyze software requirements."""
    data = request.json
    requirements_text = data.get("requirements", "")
    analysis = analyze_requirements(requirements_text)
    return jsonify({"analysis": analysis})

@app.route("/predict_risk", methods=["POST"])
def risk():
    """Endpoint to predict project risk."""
    data = request.json
    complexity = data.get("complexity", 3)
    team_size = data.get("team_size", 5)
    timeline_weeks = data.get("timeline_weeks", 12)
    risk = predict_risk(complexity, team_size, timeline_weeks)
    return jsonify({"risk_prediction": risk})

if __name__ == "__main__":
    app.run(debug=True)
