import json

class Request(object):
    """Clase para obtener datos del request de django

    Args:
        request (Request): Es un objeto de la clase Request de django
    """

    def __init__(self, request):
        self.__request = request

    @property
    def data(self):
        """dict: Metodo para obtener los datos dependiendo del metodo del request"""

        request = self.__request
        print "hola"
        print request.body

        if request.method == 'POST':
            return json.loads(request.body)
        elif request.method == 'GET':
            return request.GET.dict()

