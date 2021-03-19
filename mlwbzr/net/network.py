from ..models import Response
from ..exceptions import *
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
    if response.query_status == 'ok':
        return response
    elif response.query_status == 'http_post_expected':
        raise HttpPostException('The API expected a HTTP POST request')
    elif response.query_status == 'illegal_sha256_hash':
        raise IncorrectHashException('Illegal SHA256 hash provided')
    elif response.query_status == 'no_sha256_hash':
        raise IncorrectHashException('No SHA256 hash provided')
    elif response.query_status == 'file_not_found':
        raise FileNotKnownException('The file was not found or is unknown to MalwareBazaar')
    elif response.query_status == 'hash_not_found':
        raise FileNotKnownException('The file (hash) you wanted to query is unknown to MalwareBazaar')
    elif response.query_status == 'no_hash_provided':
        raise IncorrectHashException('You did not provide hash')
    elif response.query_status == 'file_expected':
        raise FileNameRequiredException('You did not send any file')
    elif response.query_status == 'user_blacklisted':
        raise NoApiKeyException('Your API key is blacklisted. Please contact coSntacPtAmeM@abuse.ch (remove all capital letters)')
    elif response.query_status == 'unknown_api_key':
        raise NoApiKeyException('You did not provide a correct API key')
    elif response.query_status == 'signature_not_found':
        raise SignatureException('The signature you wanted to query is unknown to MalwareBazaar')
    elif response.query_status == 'illegal_signature':
        raise SignatureException('The text you provided is not a valid signature')
    elif response.query_status == 'no_signature_provided':
        raise SignatureException('You did not provide a signature')
    elif response.query_status == 'no_results':
        raise NoResultsException('Your query yield no results')
    elif response.query_status == 'clamav_not_found':
        raise NoResultsException('The clamav signature you wanted to query is unknown to MalwareBazaar')
    elif response.query_status == 'illegal_clamav':
        raise ClamAVException('The text you provided is not a valid ClamAV signature')
    elif response.query_status == 'no_clamav_provided':
        raise ClamAVException('You did not provide a clamav signature')
    elif response.query_status == 'illegal_tlsh':
        raise NoResultsException('Illegal tlsh hash')
    elif response.query_status == 'no_tlsh':
        raise NoResultsException('Illegal telfhash')
    elif response.query_status == 'yara_not_found':
        raise ClamAVException('The yara_rule you wanted to query is unknown to MalwareBazaar')
    elif response.query_status == 'illegal_yara_rule':
        raise NoResultsException('The text you provided is not a valid yara_rule')
    elif response.query_status == 'no_yara_rule_provided':
        raise NoResultsException('You did not provide a yara_rule')
    elif response.query_status == 'illegal_issuer_cn':
        raise ClamAVException('The value you provided is not a valid issuer_cn')
    elif response.query_status == 'no_issuer_cn':
        raise NoResultsException('You did not provide a issuer_cn')
    elif response.query_status == 'file_already_known':
        raise BazaarException('File is already known')
    elif response.query_status == 'permission_denied':
        raise BazaarException('You can change only files submited by yourself')
    else:
        return response
        
