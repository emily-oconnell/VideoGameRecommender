# Kelly Romer

import requests
from igdb.wrapper import IGDBWrapper
import json

# Get Access Token
def get_token():
    client_id = '8kx354hpu7lzs6ga7c1ktafopq30qq'
    client_secret = 'yucgxc2bqiobcn2pfadu5bui5amuan'
    body = {
        'client_id': client_id,
        'client_secret': client_secret,
        "grant_type": 'client_credentials'
    }
    r = requests.post('https://id.twitch.tv/oauth2/token', body)
    keys = r.json()
    return keys['access_token']

access_token = get_token()

# Create Wrapper
wrapper = IGDBWrapper('8kx354hpu7lzs6ga7c1ktafopq30qq', access_token)

# JSON API request
params = ['genres', 'themes', 'game_modes', 'platforms', 'keywords']
for item in params:
    byte_array = wrapper.api_request(item, 'fields id, name; limit 500;')
    data = json.loads(byte_array)
    with open(item+'_to_ids.json', 'w') as outfile:
        json.dump(data, outfile, indent=4)

