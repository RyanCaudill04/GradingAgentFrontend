from django.shortcuts import render

# Create your views here.
import requests
from django.http import JsonResponse

def fetch_data_from_fastapi(request):
    fastapi_url = "http://fastapi:8001/"  # Adjust URL as needed

    try:
        response = requests.get(fastapi_url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse(data)
