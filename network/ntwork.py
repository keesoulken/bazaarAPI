from mwbzr import Response
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
        return Response.parseResponse({'query_status': 'ok', 'data': _zipfile})
    if 'json' in ct:
        _data = resp.json()
        return Response.parseResponse(_data)