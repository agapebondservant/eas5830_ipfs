import requests
import json

api_key='eaec48abcae67b71e54d'
api_secret='7f691420d756fbc887f77dfb9a25a23aaa78ae1cb2a39860fa84375fdb6b1551'
jwt='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySW5mb3JtYXRpb24iOnsiaWQiOiI3ZGVkZjdmZi1mZWFiLTQzOTItYmZlMi05ODYxZjg3ZWQxMWIiLCJlbWFpbCI6Im9hd29mb2x1QHNlYXMudXBlbm4uZWR1IiwiZW1haWxfdmVyaWZpZWQiOnRydWUsInBpbl9wb2xpY3kiOnsicmVnaW9ucyI6W3siZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiRlJBMSJ9LHsiZGVzaXJlZFJlcGxpY2F0aW9uQ291bnQiOjEsImlkIjoiTllDMSJ9XSwidmVyc2lvbiI6MX0sIm1mYV9lbmFibGVkIjpmYWxzZSwic3RhdHVzIjoiQUNUSVZFIn0sImF1dGhlbnRpY2F0aW9uVHlwZSI6InNjb3BlZEtleSIsInNjb3BlZEtleUtleSI6ImVhZWM0OGFiY2FlNjdiNzFlNTRkIiwic2NvcGVkS2V5U2VjcmV0IjoiN2Y2OTE0MjBkNzU2ZmJjODg3Zjc3ZGZiOWEyNWEyM2FhYTc4YWUxY2IyYTM5ODYwZmE4NDM3NWZkYjZiMTU1MSIsImV4cCI6MTc4MzA0NjYyOX0.Y-M-9tlsLugpcKGJZhcIwFnct0_u3IzdQDTwFTZMZg0'
gateway = "emerald-efficient-lungfish-604.mypinata.cloud"
gateway_key = 'a0-eUDrd0ZVRRL4TTOUlfXruyD4_WgjN8H358NowODwGE5GJKvsmAI7gTux1UJps'

def pin_to_ipfs(data):
    assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
    #YOUR CODE HERE
    # with open('output.txt', 'w+') as f:
    #     json.dump(data, f)
    #     response = requests.post(f"https://uploads.pinata.cloud/v3/files", files={'file':'output.txt'}, headers={"Authorization": f"Bearer {jwt}"})
    #     cid = response.json()['data']['cid']
    #     return cid
    url = 'https://api.pinata.cloud/pinning/pinJSONToIPFS'
    body = {"pinataOptions": {"cidVersion": 1}, "pinataContent": data}
    response = requests.post(url, json=body, headers={"Authorization": f"Bearer {jwt}"})
    with open(f'output.txt', 'a+') as f:
        f.write(response.text)
    return response.json()['IpfsHash']

def get_from_ipfs(cid,content_type="json"):
    assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
    #YOUR CODE HERE	
    url = f"https://{gateway}/ipfs/{cid}"
    # url = f"https://api.pinata.cloud/data/pinList"
    # response = requests.get(url, headers={"cid":cid, "pinata_api_key": api_key, "pinata_secret_api_key": api_secret})
    response = requests.get(url, headers={"cid":cid, "Authorization": f"Bearer {jwt}"})
    with open(f'debug{cid}.txt', 'a+') as f2:
        f2.write(response.text)
    data = response.json()
    assert isinstance(data,dict), f"get_from_ipfs should return a dict"
    return data
