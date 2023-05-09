import requests
import os

BEARER = os.getenv("API_Bearer_Sheety_Repl.it")
USERNAME = os.getenv("API_Username_Sheety")

PROJECT = 'flightDealsUsers'
SHEETY = 'users'

base_url = 'https://api.sheety.co'


def post_new_row(first_name, last_name, email):
        bearer_headers = {
            'Authorization': f'Bearer {BEARER}',
        }

        sheet_endpoint = f'{base_url}/{USERNAME}/{PROJECT}/{SHEETY}/'
        sheet_inputs = {
            "price":
                {
                 'firstname': first_name,
                 'lastname': last_name,
                 'email': email
                }
            }
        response = requests.post(sheet_endpoint, json=sheet_inputs, headers=bearer_headers)
        response.raise_for_status()
        print(response.text)