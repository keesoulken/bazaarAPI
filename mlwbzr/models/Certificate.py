class Cerificate():
    """
    "time_stamp": "2020-11-02 08:33:54",
    "serial_number": "6CFA5050C819C4ACBB8FA75979688DFF",
    "thumbprint": "E7241394097402BF9E32C87CADA4BA5E0D1E9923F028683713C2F339F6F59FA9",
    "thumbprint_algorithm": "SHA256",
    "subject_cn": "Elite Web Development Ltd.",
    "issuer_cn": "Sectigo RSA Code Signing CA",
    "valid_from": "Jul  2 00:00:00 2020 GMT",
    "valid_to": "Jul  2 23:59:59 2021 GMT",
    "cscb_listed": true,
    "cscb_reason": "CobaltStrike"
    """
    def __init__(self, **kwargs): 
        for key in kwargs:
            setattr(self, key, kwargs[key]) 