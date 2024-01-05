import requests
import json

def get_embeddings(endpoint, secret_key, deployment_name, text_content):
    # Set up headers, typically including authorization
    headers = {
        "Authorization": f"Bearer {secret_key}",
        "Content-Type": "application/json"
    }

    # This is an assumption based on typical API design, but you need the exact payload format
    data = {
        "deploymentName": deployment_name,
        "textContent": text_content
    }

    response = requests.post(endpoint, headers=headers, data=json.dumps(data))

    # Ensure the request was successful
    if response.status_code == 200:
        return response.json()["data"][0]["embedding"]
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

# Usage
endpoint = "https://devdiv-test-playground.openai.azure.com/"  # Replace with your endpoint
secret_key = "953cb4f4ee"     # Replace with your secret key
deployment_name = "text-embedding-ada-002"  # Replace with your deployment name
text_content = "This is the text that we're testing. Please work and give me the correct embeddings."  # Replace with the content you want embeddings for

embeddings = get_embeddings(endpoint, secret_key, deployment_name, text_content)
print(embeddings)