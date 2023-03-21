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
    response = requests.post(
        url, json={"prompt": payload, "restoreFaces": True}, headers=headers)
    print(response.text)
    print(response.json())


print(generate_random_image(
    "Scottish Warriors doing the Highland Charge"))


def list_inference_jobs(model_id):
    configure()
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {os.getenv('api_key')}"
    }
    url = f"https://api.tryleap.ai/api/v1/images/models/{model_id}/inferences"
    response = requests.get(url, headers=headers)
    print(response.text)


def delete_image(model_id):
    configure()
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {os.getenv('api_key')}"
    }
    url = f"https://api.tryleap.ai/api/v1/images/models/{model_id}"
    response = requests.delete(url, headers=headers)
    print(response.text)
