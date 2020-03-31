from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):

    def get(self, request, format=None):

        an_apiview = [
            'View 1',
            'View 2',
            'View 3',
            'View 4',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})
