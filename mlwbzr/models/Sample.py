class Sample():
    """
        fields are likely: ['anonymous', 
        'code_sign', 'comment', 'comments', 
        'delivery_method', 'file_information', 'file_name', 
        'file_size', 'file_type', 'file_type_mime', 
        'first_seen', 'fromjson', 'fromjsonlist', 
        'imphash', 'intelligence', 'last_seen', 
        'md5_hash', 'ole_information', 'origin_country', 
        'reporter', 'sha1_hash', 'sha256_hash', 
        'sha3_384_hash', 'signature', 'ssdeep', 'tags', 
        'telfhash', 'tlsh', 'vendor_intel', 'yara_rules']
    """
    def __init__(self, **kwargs): 
        for key in kwargs:
            setattr(self, key, kwargs[key]) 
    
    @staticmethod
    def fromjson(data):
        return Sample(**data[-1])

    @staticmethod
    def fromjsonlist(data):
        samples = []
        for d in data:
            samples.append(Sample(**d))
        return samples
