import json

class Request(object):

    data = None

    def __init__(self, request):
        self.data = self.getData(request)

    def getData(self, request):
        if request.method == 'POST':
            return json.loads(request.body)
        elif request.method == 'GET':
            return request.GET.dict()

