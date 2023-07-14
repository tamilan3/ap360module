import requests
import json
from end_point import projects_endpoint,user_endpoint
from pprint import pprint
from dotenv import load_dotenv
import os

load_dotenv()
apikey = os.getenv("apikey")

def projects_list():
    headers={'Authorization': f'Bearer {apikey}','Content-Type': 'application/json'}
    response=requests.get(projects_endpoint,headers=headers)
    response=response.json()
    remove_key="ringId"
    for i in response:
        del i['$type']
    pprint(response, indent=4)

projects_list()    