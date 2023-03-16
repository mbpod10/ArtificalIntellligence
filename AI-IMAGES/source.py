import requests
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


configure()

url = "https://api.tryleap.ai/api/v1/images/models/8b1b897c-d66d-45a6-b8d7-8e32421d02cf/inferences"

payload = {"prompt": "A cat in cyberpunk world"}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": f"Bearer {os.getenv('api_key')}"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
