from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

# Your endpoint URL and verification token
ENDPOINT_URL = "https://your-domain.com"  # Replace with your deployed endpoint
VERIFICATION_TOKEN = "your_32_to_80_char_token_here"  # Replace with your token

@app.route("/", methods=["GET"])
def ebay_challenge():
    challenge_code = request.args.get("challenge_code")
    if not challenge_code:
        return "No challenge code provided", 400

    # Compute SHA256 hash: challengeCode + verificationToken + endpoint
    hash_input = (challenge_code + VERIFICATION_TOKEN + ENDPOINT_URL).encode('utf-8')
    challenge_response = hashlib.sha256(hash_input).hexdigest()

    # Return JSON
    return jsonify({"challengeResponse": challenge_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)  # Ensure port matches Render config
