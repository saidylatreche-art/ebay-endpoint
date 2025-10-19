from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

VERIFICATION_TOKEN = "X9f7vR2pQ8kLm5tY1sDz4Wb6NcGjH0aVqUrBx3FhKpL"
ENDPOINT_URL = "https://ebay-endpoint-8t69.onrender.com"  # Must match the eBay registered endpoint

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if request.method == 'GET':
        # 🧠 eBay sends a challenge_code here
        challenge_code = request.args.get('challenge_code')
        if challenge_code:
            # compute SHA256(challengeCode + verificationToken + endpoint)
            data = (challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL).encode('utf-8')
            hashed = hashlib.sha256(data).hexdigest()

            # respond with JSON object { "challengeResponse": "<hash>" }
            return jsonify({"challengeResponse": hashed}), 200, {'Content-Type': 'application/json'}
        else:
            return jsonify({"message": "No challenge_code provided"}), 400

    elif request.method == 'POST':
        # 📦 Handle deletion/closure notifications
        data = request.get_json(force=True, silent=True)
        print("Received POST notification:", data)
        return jsonify({"status": "received"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
