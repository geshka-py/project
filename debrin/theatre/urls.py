from django.urls import path
from .views import index, performance


urlpatterns = [
    path('index', index),
    path('<int:tid>', performance, name='performance')
]
