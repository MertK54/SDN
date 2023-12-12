# json tipi verilerin alınması için json kütüphanesinin çağrılması
# request kütüphanesi, Python dilinde HTTP istekleri yapmak için kullanılan bir kütüphanedir

import json
import requests

controller_ip = "127.0.0.1"

# flow'lerin oluşturulması
flows = [
    {
        "switch": "00:00:00:00:00:00:00:01", 	# switch adress
        "name": "flow1",			# akış ismi
        "priority": "32768",			# yeni atanan akışın öncelik derecesi
        "eth_type": "0x800",			# "eth_type": "0x800" ifadesi, bir Ethernet paketinin bir IP paketi taşıdığını belirtir
        "in_port": "1",				# switch'in giriş port numarası belirtilir
        "active": "true",			# burası true olduğu durumda flow etkinleştirilir
        "actions": "output=2,output=3"		# switch'in çıkış port numarası belirtilir
    },
    {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "flow2",
        "priority": "32768",
        "eth_type": "0x800",
        "in_port": "2",
        "active": "true",
        "actions": "output=1"
    },
    {
        "switch": "00:00:00:00:00:00:00:01",
        "name": "flow3",
        "priority": "32768",
        "eth_type": "0x800",
        "in_port": "3",
        "active": "true",
        "actions": "output=1"
    },
    {
        "switch": "00:00:00:00:00:00:00:02",
        "name": "flow4",
        "priority": "32768",
        "eth_type": "0x800",
        "in_port": "1",
        "active": "true",
        "actions": "output=2"
    },
    {
        "switch": "00:00:00:00:00:00:00:02",
        "name": "flow5",
        "priority": "32768",
        "eth_type": "0x800",
        "in_port": "2",
        "active": "true",
        "actions": "output=1"
    },
    {
        "switch": "00:00:00:00:00:00:00:03",
        "name": "flow6",
        "priority": "32768",
        "eth_type": "0x800",
        "in_port": "1",
        "active": "true",
        "actions": "output=2"
    },
    {
        "switch": "00:00:00:00:00:00:00:03",
        "name": "flow7",
        "priority": "32768",
        "eth_type": "0x800",
        "in_port": "2",
        "active": "true",
        "actions": "output=1"
    },
    {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow8",
        "priority": "32768",
        "eth_type": "0x800",
        "in_port": "1",
        "active": "true",
        "actions": "output=3"
    },
    {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow9",
        "priority": "32768",
        "eth_type": "0x800",
        "in_port": "2",
        "active": "true",
        "actions": "output=3"
    },
    {
        "switch": "00:00:00:00:00:00:00:04",
        "name": "flow10",
        "priority": "32768",
        "eth_type": "0x800",
        "in_port": "3",
        "active": "true",
        "actions": "output=2"
    }
    
]


# http protocolü için url'in belirtilmesi
url = f"http://{controller_ip}:8080/wm/staticflowentrypusher/json"

#Bu ifade, bir HTTP isteğinin içeriğinin türünü belirtir ve bu ifade sayesinde sunucu tarafından istek içeriğinin nasıl işleneceği belirlenir
headers = {"Content-Type": "application/json"}

# flow'ler http protocolü üzerinde controller'e gönderilir
for flow in flows:
    response = requests.post(url, data=json.dumps(flow), headers=headers)
    print(response.text)
