import json
import requests

# Replace with the IP address of your Floodlight controller
controller_ip = "127.0.0.1"

# Define the flows to be created
flows = [
    {
        "switch": "00:00:00:00:00:00:00:01", 
    	"name": "flow-1", 
   	"priority": "32768",  
    	"in_port": "1",  
    	"eth_type": "0x800",  
    	"ipv4_src": "10.0.0.1",  
    	"ipv4_dst": "10.0.0.2",  
    	"nw_proto": "1",  
    	"nw_tos": "0",  
    	"active": "true",  
    	"actions": "output=2"  
    },
    {
        "switch": "00:00:00:00:00:00:00:01", 
    	"name": "flow-2", 
   	"priority": "32768",  
    	"in_port": "1",  
    	"eth_type": "0x800",  
    	"ipv4_src": "10.0.0.1",  
    	"ipv4_dst": "10.0.0.2",  
    	"nw_proto": "1",  
    	"nw_tos": "1",  
    	"active": "true",  
    	"actions": "output=3"
    }
]

# Send a POST request to the Floodlight controller to create the flows
url = f"http://{controller_ip}:8080/wm/staticflowentrypusher/json"
headers = {"Content-Type": "application/json"}
for flow in flows:
    response = requests.post(url, data=json.dumps(flow), headers=headers)
    print(response.text)
