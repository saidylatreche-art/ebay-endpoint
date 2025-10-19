from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace this with the "verification token" shown in eBay's developer console
EBAY_VERIFICATION_TOKEN = "your_verification_token_here"

@app.route("/", methods=["GET"])
def verify():
    challenge_code = request.args.get("challenge_code")
    if challenge_code:
        return jsonify({"challengeResponse": challenge_code + EBAY_VERIFICATION_TOKEN})
    return "eBay Endpoint Running", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
