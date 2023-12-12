import json
import requests

# Replace with the IP address of your Floodlight controller
controller_ip = "127.0.0.1"

# Define the flows to be created
flows = [
    {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "flow1",
        "cookie": "0",
        "priority": "32768",
        "eth_type": "0x800",
        "in_port": "1",
        "active": "true",
        "actions": "output=2,output=3"
    },
    {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "flow2",
        "cookie": "0",
        "priority": "32768",
        "eth_type": "0x800",
        "in_port": "2",
        "active": "true",
        "actions": "output=3,output=1"
    },
    {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "flow3",
        "cookie": "0",
        "priority": "32768",
        "eth_type": "0x800",
        "in_port": "3",
        "active": "true",
        "actions": "output=2,output=3"
    }
]

# Send a POST request to the Floodlight controller to create the flows
url = f"http://{controller_ip}:8080/wm/staticflowentrypusher/json"
headers = {"Content-Type": "application/json"}
for flow in flows:
    response = requests.post(url, data=json.dumps(flow), headers=headers)
    print(response.text)
