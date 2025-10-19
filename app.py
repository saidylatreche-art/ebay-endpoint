from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    challenge = request.args.get("challenge_code")
    if challenge:
        # Respond with the challenge code for eBay verification
        return challenge, 200
    return "eBay Endpoint is running!", 200

@app.route("/notifications", methods=["POST"])
def notifications():
    data = request.get_json()
    print("Received notification:", data)
    return {"status": "received"}, 200

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
