from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet, basename = "hello-viewset")
router.register('profile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)


urlpatterns = [
    path('hello/', views.HelloAppView.as_view(), name="hello"),
    path('login/', views.UserLoginAPIView.as_view()),
    path('', include(router.urls)),
]
