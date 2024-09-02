from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloAppView(APIView):
    """Hello World View"""

    serializers_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """Return only Hello World as Response"""

        an_apiview = [
            'Uses Http methods as functions like get post put delete patch',
            'It is similar to traditional django view',
            'Gives more control over api calls',
            'Can maps URLs'
        ]

        return Response({'msg':"HelloWolrd", 'an_apiview': an_apiview})
    
    def post(self, request):
        """post request to get Hello with our name"""
        serializer = self.serializers_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'Hello {name}'
            return Response({'msg':msg})
        else:
            return Response(
                serializer.errors, 
                status = status.HTTP_400_BAD_REQUEST
            )
    
    def put(self,request, pk=None):
        """Hanlde PUT methods"""
        return Response({"msg":"This is PUT method, Update object direclty"})
    
    def patch(self,request, pk=None):
        """Hanlde PATCH methods"""
        return Response({"msg":"This is PATCH method, only update fileds of an object"})
    
    def delete(self, request, pk=None):
        """Delete method for delete"""
        return Response({'msg':"Delete method for Hello"})