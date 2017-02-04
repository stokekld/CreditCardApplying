from django.http import HttpResponse
from django.http import JsonResponse


class UsuarioViews(object):
    def prueba(self, request):
        # return HttpResponse("Hola mundo")
        return JsonResponse({'foo':'bar'})
