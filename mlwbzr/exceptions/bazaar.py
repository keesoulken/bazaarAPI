class BazaarException(Exception):
    pass

class IncorrectHashException(BazaarException):
    pass

class NoApiKeyException(BazaarException):
    pass

class SignatureException(BazaarException):
    pass

class NoResultsException(BazaarException):
    pass

class ClamAVException(BazaarException):
    pass

class YaraException(BazaarException):
    pass

class IssuerCNException(BazaarException):
    pass

