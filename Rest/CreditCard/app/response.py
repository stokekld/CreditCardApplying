from rest_framework.response import Response as RFResponse
from rest_framework import status

class Response(object):

    class Inner:

        def __init__(self, data, status, error):

            self.data = data
            self.error = error
            self.status = status

    def __new__(self, data = {}, status=status.HTTP_200_OK, error=""):

        response = self.Inner(data, status, error)

        return RFResponse(response.__dict__, status=response.status)

