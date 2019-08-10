#Apartado 8.30, Apartado 9.39 -> Add , include
from django.urls import path, include
from profiles_api import views
#Apartado 9.39
from rest_framework.routers import DefaultRouter

#Apartado 9.39
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
#Apartado 10.46
router.register('profile', views.UserProfileViewSet)
#Apartado 12.61
router.register('feed', views.UserProfileFeedViewSet)

#Apartado 9.39
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    #Apartado 11.53
    path('login/', views.UserLoginApiView.as_view()),
    #Apartado 9.39
    path('', include(router.urls)),
]
