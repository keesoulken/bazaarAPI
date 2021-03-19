#!/usr/bin/env python3
from .net.network import send_post
from .models import *
from .exceptions import NoApiKeyException, FileNameRequiredException

from typing import Dict, Optional

class Client():
    def __init__(self, api_key=None):
        self.api_key = api_key
        self.api_url = "https://mb-api.abuse.ch/api/v1/"

    def __query(self, **data) -> Optional[Dict]:
        r = send_post(self.api_url, self.api_key, data=data)
        if r.data is not None:
            return r.data
        else:
            return None
    
    def __query_list(self, **data) -> [Sample]:
        response_data = self.__query(**data)
        if response_data is not None:
            return Sample.fromjsonlist(response_data)
        else:
            return None

    def __query_one(self, **data) -> Sample:
        response_data = self.__query(**data)
        if response_data is not None:
            return Sample.fromjson(response_data)
        else:
            return None

    def send_file(self, file, anonymous=0, tags=None, references=None, context=None, delivery_method=None) -> Response:
        if self.api_key is None:
            raise NoApiKeyException
        if file is None:
            raise FileNameRequiredException
        data = {}
        if anonymous == 1:
            data['anonymous'] = 1
        if delivery_method is not None:
            data['delivery_method'] = delivery_method
        if type(tags) is list and len(tags) > 0:
            data['tags'] = tags
        if context is not None and type(context) is dict:
            data['context'] = context
        if references is not None and type(references) is dict:
            data['references'] = references

        response = send_post(self.api_url, self.api_key, filename=file, data=data)
        return response

    
    def get_file(self, sha256_hash) -> Response:
        if self.api_key is None:
            raise NoApiKeyException
        data = {'query': 'get_file'}
        data['sha256_hash'] = sha256_hash
        return send_post(self.api_url, self.api_key, data=data)

    def get_info(self, hash) -> Sample:
        if self.api_key is None:
            raise NoApiKeyException
        data = {'query': 'get_info'}
        data['hash'] = hash
        r = send_post(self.api_url, self.api_key, data=data)
        if r.data is not None:
            return Sample.fromjson(r.data)
        else:
            return None

    def update(self, sha256_hash, key, value) -> Response:
        if self.api_key is None:
            raise NoApiKeyException
        data = {'query': 'update'}
        data['sha256_hash'] = sha256_hash
        data['key'] = key
        data['value'] = value
        r = send_post(self.api_url, self.api_key, data=data)
        return r

    def add_comment(self, sha256_hash, comment) -> Response:
        if self.api_key is None:
            raise NoApiKeyException
        data = {'query': 'add_comment'}
        data['sha256_hash'] = sha256_hash
        data['comment'] = comment
        r = send_post(self.api_url, self.api_key, data=data)
        return r

    def get_recent(self, selector) -> [Sample]:
        if self.api_key is None:
            raise NoApiKeyException
        data = {'query': 'get_recent'}
        data['selector'] = selector
        r = send_post(self.api_url, self.api_key, data=data)
        if r.data is not None:
            return Sample.fromjsonlist(r.data)
        else:
            return None
    
    def get_taginfo(self, tag, limit=50) -> [Sample]:
        return self.__query_list(query='get_taginfo', tag=tag, limit=limit)

    def get_siginfo(self, signature, limit=50) -> [Sample]:
        return self.__query_list(query='get_siginfo', signature=signature, limit=limit)

    def get_clamavinfo(self, signature, limit=50) -> [Sample]:
        return self.__query_list(query='get_clamavinfo', clamav=signature, limit=limit)