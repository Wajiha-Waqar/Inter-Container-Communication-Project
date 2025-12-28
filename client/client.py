import requests
import time

url = "http://api:5000/send"

for i in range(20):
    try:
        print("Attempt", i + 1, ": contacting API...")
        response = requests.post(url, json={"message": "Hello from Client"})
        print("Server response:", response.text)
        break
    except requests.exceptions.ConnectionError:
        print("API not ready yet, waiting...")
        time.sleep(2)
else:
    print("API never became available")
