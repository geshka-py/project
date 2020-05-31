from django.urls import path
from .views import library, film

urlpatterns = [
    path('library', library),
    path('<int:fid>', film, name='film'),
]
