from flask import Flask, request, jsonify
from services.blackout_service import risk_of_blackout

app = Flask(__name__)

@app.route("/api/v1/blackout-risk", methods=["GET"])
def get_blackout_risk():
    """
    Exemplo de uso:
    /api/v1/blackout-risk?lat=-23.55&lon=-46.63
    """
    try:
        lat = float(request.args.get("lat"))
        lon = float(request.args.get("lon"))
        result = risk_of_blackout(lat, lon)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
