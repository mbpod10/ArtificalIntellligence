import requests
from dotenv import load_dotenv
import os


def configure():
    load_dotenv()


def generate_random_image(payload):
    configure()
    url = "https://api.tryleap.ai/api/v1/images/models/8b1b897c-d66d-45a6-b8d7-8e32421d02cf/inferences"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {os.getenv('api_key')}"
    }
    response = requests.post(url, json={"prompt": payload}, headers=headers)
    print(response.text)


print(generate_random_image("Blackbeard on the Queen Anne's Revenge"))
