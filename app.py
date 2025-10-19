from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

VERIFICATION_TOKEN = "X9f7vR2pQ8kLm5tY1sDz4Wb6NcGjH0aVqUrBx3FhKpL"
ENDPOINT_URL = "https://ebay-endpoint-8t69.onrender.com"  # Must match the eBay registered endpoint

@app.route("/", methods=["GET"])
def verify():
    challenge_code = request.args.get("challenge_code")
    if challenge_code:
        # Compute SHA-256 hash: challengeCode + verificationToken + endpoint
        m = hashlib.sha256()
        m.update(challenge_code.encode('utf-8'))
        m.update(VERIFICATION_TOKEN.encode('utf-8'))
        m.update(ENDPOINT_URL.encode('utf-8'))
        response_hash = m.hexdigest()
        return jsonify({"challengeResponse": response_hash})
    return "No challenge code received", 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


