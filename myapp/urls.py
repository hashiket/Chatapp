from django.urls import path, include
from .views import  UserRegistrationView, UserLoginView,UserChangePasswordView, GroupViewSet, ChatViewSet
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('group', views.GroupViewSet, basename='group')
router.register('createchat', views.ChatViewSet, basename='chat')



urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register' ),
    path('login/', UserLoginView.as_view(), name='login' ),
    path('changepassword/', UserChangePasswordView.as_view(), name='changepassword' ),
    path('', include(router.urls)),


]
