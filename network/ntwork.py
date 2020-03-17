from mwbzr import Response
from exceptions import HttpPostException, IncorrectHashException, FileNotKnownException, FileNameRequiredException, NoApiKeyException
import requests
import json

def send_post(endpoint, api_key, filename=None, data=None) -> Response:
    files = {}
    headers = {'API-KEY' : api_key}
    if filename is None:
        resp = requests.post(endpoint, headers=headers, data=data)
    else:
        files['file'] = (open(filename, 'rb'))
        files['data'] = (None, json.dumps(data), 'application/json')
        resp = requests.post(endpoint, headers=headers, files=files)

    ct = resp.headers['Content-Type']
    if 'zip' in ct:
        _zipfile = resp.content
        response = Response.parseResponse({'query_status': 'ok', 'data': _zipfile})
    if 'json' in ct:
        _data = resp.json()
        response = Response.parseResponse(_data)
    print(response.query_status)
    if response.query_status == 'http_post_expected':
        raise HttpPostException('The API expected a HTTP POST request')
    if response.query_status == 'illegal_sha256_hash':
        raise IncorrectHashException('Illegal SHA256 hash provided')
    if response.query_status == 'no_sha256_hash':
        raise IncorrectHashException('No SHA256 hash provided')
    if response.query_status == 'file_not_found':
        raise FileNotKnownException('The file was not found or is unknown to MalwareBazaar')
    if response.query_status == 'hash_not_found':
        raise FileNotKnownException('The file (hash) you wanted to query is unknown to MalwareBazaar')
    if response.query_status == 'no_hash_provided':
        raise IncorrectHashException('You did not provide hash')
    if response.query_status == 'file_expected':
        raise FileNameRequiredException('You did not send any file')
    if response.query_status == 'user_blacklisted':
        raise NoApiKeyException('Your API key is blacklisted. Please contact coSntacPtAmeM@abuse.ch (remove all capital letters)')
    if response.query_status == 'unknown_api_key':
        raise NoApiKeyException('You did not provide a correct API key')
    return response