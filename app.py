from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage for received webhooks
webhooks = []

# Example route to receive webhooks
@app.route('/webhook', methods=['POST'])
def webhook():
    # Parse the incoming JSON payload
    data = request.json
    
    # Store the webhook data
    webhooks.append(data)
    
    # Log the received data
    print(f"Received webhook: {data}")
    
    # Respond with a status code and message
    return jsonify({"status": "success", "message": "Webhook received"}), 200

# Route to display received webhooks
@app.route('/')
def index():
    return render_template('index.html', webhooks=webhooks)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
