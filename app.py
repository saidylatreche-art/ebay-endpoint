from flask import Flask, request, jsonify

app = Flask(__name__)

# Simple health check route
@app.route("/")
def home():
    return "eBay Endpoint is running!"

# Endpoint to receive eBay notifications
@app.route("/notifications", methods=["POST"])
def notifications():
    data = request.get_json()
    print("Received notification:", data)  # for debugging
    return jsonify({"status": "received"}), 200

if __name__ == "__main__":
    # Bind to Render's port
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
