from django.urls import path
from .views import fetch_data_from_fastapi

urlpatterns = [
    path('fetch/', fetch_data_from_fastapi, name='fetch_data'),
]
