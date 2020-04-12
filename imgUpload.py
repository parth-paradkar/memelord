import json
import os
import requests
from dotenv import (load_dotenv, find_dotenv)

load_dotenv(find_dotenv())

def uploadImgImgur(url):
    r = requests.get(url)
    data = r.content
    
    client_id = os.getenv("IMGUR_CLIENT_ID")
    
    imgur_upload_url = "https://api.imgur.com/3/image"
    headers = {'Authorization': 'Client-ID {}'.format(client_id), "content-type": "multipart/form-data"}
    r = requests.post(imgur_upload_url, headers=headers, data=data)
    
    try:
        link = r.json()['data']['link']
    except KeyError:
        link = "Failed"
    
    return link
