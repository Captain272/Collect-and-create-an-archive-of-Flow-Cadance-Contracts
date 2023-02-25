# References : https://developers.flow.com/http-api/

import requests

url = "https://rest-testnet.onflow.org/v1/blocks"
params = {'start_height':[95630405],'end_height':[95630406]}
headers = {'user-agent': 'my-app/0.0.1'}
response = requests.get(url, params=params, headers=headers)
if response.status_code:
    data = response.json()
    print(data)
else:
    print("Error retrieving data.")