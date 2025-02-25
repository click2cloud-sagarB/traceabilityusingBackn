import requests
import time

BASE_URL = "http://localhost:5000/api"

def update_stage(product_id, stage, location):
    payload = {
        "message": {
            "order": {
                "id": product_id,
                "item": {
                    "id": f"{stage.replace(' ', '_')}_item",
                    "status": stage,
                    "location": location
                }
            }
        }
    }
    response = requests.post(f"{BASE_URL}/update", json=payload)
    print("Update Response:", response.json())

def track_product(product_id):
    response = requests.get(f"{BASE_URL}/track", params={"product_id": product_id})
    print("Track Response:", response.json())

if __name__ == '__main__':
    product_id = "coffee-123"
    
    # Stage 1: Harvested at Jammu Farm
    update_stage(product_id, "harvested", "Jammu Farm")
    time.sleep(1)
    
    # Stage 2: Processed at Mumbai Processor
    update_stage(product_id, "processed", "Mumbai Processor")
    time.sleep(1)
    
    # Stage 3: Packaged at Mumbai Facility
    update_stage(product_id, "packaged", "Mumbai Facility")
    time.sleep(1)
    
    # Stage 4: Shipped to Pune Distribution Center
    update_stage(product_id, "shipped", "Pune Distribution Center")
    time.sleep(1)
    
    # Stage 5: Delivered to Pune Retailer
    update_stage(product_id, "delivered", "Pune Retailer")
    time.sleep(1)
    
    # Stage 6: Served at Pune Cafe (e.g., in a milkshake)
    update_stage(product_id, "served", "Pune Cafe")
    time.sleep(1)
    
    # Retrieve the full journey using the track endpoint
    track_product(product_id)
