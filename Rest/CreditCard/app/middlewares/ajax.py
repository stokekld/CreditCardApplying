from django.http import JsonResponse
from rest_framework import status

class Ajax(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if not request.is_ajax():
            return JsonResponse({'error': "El request no es ajax"}, status=status.HTTP_400_BAD_REQUEST)

        response = self.get_response(request)

        return response

