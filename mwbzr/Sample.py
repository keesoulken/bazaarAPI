class Sample():
    def __init__(self, sha256_hash=None, sha1_hash=None, md5_hash=None, first_seen=None, last_seen=None, file_name=None, file_size=None, 
    file_type=None, reporter=None, anonymous=None, signature=None, imphash=None, ssdeep=None, tags=None, delivery_method=None,
     file_type_mime=None, comment=None, intelligence=None, file_information=None, comments=None):
        self.sha256_hash = sha256_hash
        self.sha1_hash = sha1_hash
        self.md5_hash = md5_hash
        self.first_seen = first_seen
        self.last_seen = last_seen
        self.file_name = file_name
        self.file_size = file_size
        self.file_type = file_type
        self.reporter = reporter
        self.anonymous = anonymous
        self.signature = signature
        self.imphash = imphash
        self.ssdeep = ssdeep
        self.tags = tags
        self.delivery_method = delivery_method
        self.file_type_mime = file_type_mime
        self.comment = comment
        self.intelligence = intelligence
        self.file_information = file_information
        self.comments = comments
    
    @staticmethod
    def fromjson(data):
        return Sample(**data[-1])

    @staticmethod
    def fromjsonlist(data):
        samples = []
        for d in data:
            samples.append(Sample(**d))
        return samples