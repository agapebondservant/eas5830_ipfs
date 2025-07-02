import requests
import json
import uuid

api_key='af83c96cc0ff485bb901f9ed92726df3'
api_secret='p0xwRkYKBQcRfhM5bQgW6/X70Y5CmcHVAn8QzjZ5jbqEO8r3/xyEjg'
endpoint = "https://ipfs.infura.io:5001"

def pin_to_ipfs(data):
    assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
    #YOUR CODE HERE
    file_name=str(uuid.uuid4())
    with open(file_name, 'w') as f:
        f.write(str(data)) #json.dump(data, f, indent=4)
        response = requests.post(endpoint + "/api/v0/add", files={"file":file_name}, auth=(api_key, api_secret))
        cid = response.text.split(",")[1].split(":")[1].replace('"','')
        print(cid)
        return cid

def get_from_ipfs(cid,content_type="json"):
    assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
    #YOUR CODE HERE	
    url = f"{endpoint}/api/v0/cat?arg={cid}"
    response = requests.post(url, params={"arg": cid}, auth=(api_key, api_secret))
    data = response.text
    assert isinstance(data,dict), f"get_from_ipfs should return a dict"
    return data
