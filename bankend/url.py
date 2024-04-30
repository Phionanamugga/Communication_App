from django.urls import path
from .views import index, test

# map your urls 
urlpatterns = [
    path ('', index)
    path('home', index),
    path ('room', )


]

