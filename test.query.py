import requests

url = "http://127.0.0.1:5000/api/query"
data = {"question": "What is this project about?"}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Raw Response Text:", response.text)  # <-- Add this line to debug

try:
    print("Response JSON:", response.json())
except Exception as e:
    print("Error decoding JSON:", e)