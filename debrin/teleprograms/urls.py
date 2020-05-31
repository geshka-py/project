from django.urls import path
from .views import index, program

urlpatterns = [
    path('index', index),
    path('<int>:pid', program, name='program')
]