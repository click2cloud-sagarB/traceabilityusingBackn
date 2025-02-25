from flask import Flask, request, jsonify
import datetime
import os
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# In-memory storage simulating a decentralized traceability ledger.
traceability_data = {}

def get_iso_timestamp():
    return datetime.datetime.now().isoformat()

# API endpoint to update product status (simulate various stages)
@app.route('/api/update', methods=['POST'])
def update():
    """
    Expected JSON structure:
    {
      "message": {
         "order": {
             "id": "coffee-123",
             "item": {
                 "id": "some_item_id",
                 "status": "harvested",
                 "location": "Jammu Farm"
             }
         }
      }
    }
    """
    data = request.get_json()
    try:
        order = data["message"]["order"]
        product_id = order["id"]
        item = order["item"]
        stage = item["status"]
        location = item["location"]
    except KeyError:
        return jsonify({"status": "error", "message": "Invalid request format"}), 400

    if product_id not in traceability_data:
        traceability_data[product_id] = []
    
    update_entry = {
        "stage": stage,
        "location": location,
        "timestamp": get_iso_timestamp()
    }
    traceability_data[product_id].append(update_entry)
    return jsonify({"status": "success", "message": "Update recorded", "data": update_entry}), 200

# API endpoint to search for a product journey
@app.route('/api/search', methods=['GET'])
def search():
    product_id = request.args.get("product_id")
    if not product_id:
        return jsonify({"status": "error", "message": "product_id is required"}), 400
    if product_id in traceability_data:
        return jsonify({"status": "success", "data": traceability_data[product_id]}), 200
    else:
        return jsonify({"status": "error", "message": "Product not found"}), 404

# API endpoint to track the product (akin to Beckn’s "track" API)
@app.route('/api/track', methods=['GET'])
def track():
    """
    Returns full traceability information for a product in a Beckn-like format.
    Example response:
    {
      "context": {
          "action": "track",
          "transaction_id": "txn-coffee-123-1672531200",
          "timestamp": "2025-02-25T12:00:00Z",
          "bap_id": "agripilot.ai",
          "bap_uri": "https://agripilot.ai/api"
      },
      "message": {
          "order": {
              "id": "coffee-123",
              "tracking": [ ... list of updates ... ]
          }
      }
    }
    """
    product_id = request.args.get("product_id")
    if not product_id:
        return jsonify({"status": "error", "message": "product_id is required"}), 400

    if product_id in traceability_data:
        response = {
            "context": {
                "action": "track",
                "transaction_id": f"txn-{product_id}-{int(datetime.datetime.now().timestamp())}",
                "timestamp": get_iso_timestamp(),
                "bap_id": app.config.get("BAP_ID", "agripilot.ai"),
                "bap_uri": app.config.get("BAP_URI", "https://agripilot.ai/api")
            },
            "message": {
                "order": {
                    "id": product_id,
                    "tracking": traceability_data[product_id]
                }
            }
        }
        return jsonify(response), 200
    else:
        return jsonify({"status": "error", "message": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
