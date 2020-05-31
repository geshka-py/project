from django.urls import path
from .views import index, interview

urlpatterns = [
    path('index', index),
    path('<int:iid>', interview, name='interview'),
]