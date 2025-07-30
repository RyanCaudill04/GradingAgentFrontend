from django.http import JsonResponse
import requests

def call_fastapi(request):
    response = requests.get("http://localhost:8001/api/hello")
    return JsonResponse(response.json())
