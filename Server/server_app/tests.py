from django.test import TestCase

# Create your tests here.
import requests
import json

# Define the base URL for the API endpoint
base_url = "http://localhost:8000/api/"

# Define the headers for the API request
headers = {
    'Content-Type': 'application/json'
}

# Define the generate_pizza API endpoint URL
generate_pizza_url = base_url + "generate_pizza/"

# Define the get_user_data API endpoint URL
get_user_data_url = base_url + "get_user_data/"

# Define the payload for the generate_pizza API request
generate_pizza_payload = {
    "username": "test_user"
}

# Define the payload for the get_user_data API request
get_user_data_payload = {
    "username": "test_user"
}

# Send the generate_pizza API request
generate_pizza_response = requests.post(generate_pizza_url, headers=headers, data=json.dumps(generate_pizza_payload))

# Check if the generate_pizza API request was successful
if generate_pizza_response.status_code == 201:
    print("Successfully generated a pizza.")
else:
    print("Failed to generate a pizza.")

# Send the get_user_data API request
get_user_data_response = requests.post(get_user_data_url, headers=headers, data=json.dumps(get_user_data_payload))

# Check if the get_user_data API request was successful
if get_user_data_response.status_code == 200:
    # Print the returned JSON
    print(get_user_data_response.json())
else:
    print("Failed to retrieve user data.")