from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('post', views.Post),
    path('posts/<slug:slug>', views.detail),
    path('iran-map', views.IranMap),
    path('seener', views.seener),
]