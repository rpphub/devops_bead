from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json() or {}
    message = data.get("message", "")
    # Itt lehetne bonyolítani (log, időbélyeg, stb.)
    return jsonify({"echo": message})


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    # Dockerből elérhető legyen kívülről is
    app.run(host="0.0.0.0", port=8000)