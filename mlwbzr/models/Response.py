class Response():
    def __init__(self, query_status, data):
        self.query_status = query_status
        self.data = data

    @staticmethod
    def parseResponse(res_json):
        return Response(res_json['query_status'], res_json['data'] if 'data' in res_json else None)
