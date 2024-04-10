from django.urls import path
from .views import home, dataPost

urlpatterns = [
    path('', home, name='home'),
    path('add/', dataPost, name='data_post'),
]
