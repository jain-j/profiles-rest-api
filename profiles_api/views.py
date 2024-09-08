from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


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
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def put(self,request, pk=None):
        """Hanlde PUT methods"""
        return Response({"msg":"This is PUT method, Update object direclty"})
    
    def patch(self,request, pk=None):
        """Hanlde PATCH methods"""
        return Response({"msg":"This is PATCH method, only update fileds of an object"})
    
    def delete(self, request, pk=None):
        """Delete method for delete"""
        return Response({'msg':"Delete method for Hello"})


class HelloViewSet(viewsets.ViewSet):
    """View Set ------"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """gets list of objects"""
        a_viewset = [
            "Uses actions (list, create, retrieve, update, delete)",
            "Automatically maps to URL",
            "less code more features"
        ]

        return Response({"msg":"Hello from list of HelloViewSet", "a_viewset":a_viewset})
    
    def create(self, request):
        """Create hello msg new"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            msg = f'Hello {name} bhai.....'
            return Response({'msg':msg})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        """retrive method of HelloViewSet"""

        return Response({'data':"retireved data is this. GET"})
    
    def update(self,request, pk=None):
        """updating object by update mathod"""

        return Response({'data':"updated object in DB PUT"})
    
    def partial_update(self,request, pk=None):
        """object updating partially"""

        return Response({'data':"partially update data PATCH"})
    
    def destroy(self, request, pk=None):
        """object delete by this"""

        return Response({'data':"detele data DELETE"})

class UserProfileViewSet(viewsets.ModelViewSet):
    """create update user profile API with Model View Set which specially desinged for Model API"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginAPIView(ObtainAuthToken):
    """User login using authentications"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (permissions.UpdateOwnStatus,IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(user_profile = self.request.user)