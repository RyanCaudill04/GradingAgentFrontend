from django.shortcuts import render
import requests
from django.http import JsonResponse
import json

def home(request):
    return render(request, 'home.html')

def fetch_data_from_fastapi(request):
    fastapi_url = "http://fastapi:8001/"  # Adjust URL as needed

    try:
        response = requests.get(fastapi_url, timeout=5)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse(data)

def submit_grading_request(request):
    result = None
    if request.method == 'POST':
        assignment_name = request.POST.get('assignment_name')
        repo_link = request.POST.get('repo_link')
        token = request.POST.get('token')

        fastapi_url = "http://fastapi:8001/grade"
        payload = {
            "assignment_name": assignment_name,
            "repo_link": repo_link,
            "token": token
        }

        try:
            response = requests.post(fastapi_url, json=payload, timeout=30)
            response.raise_for_status()
            result = json.dumps(response.json(), indent=4)
        except requests.RequestException as e:
            result = json.dumps({"error": str(e)}, indent=4)

    return render(request, 'submit_grading_request.html', {'result': result})

def upload_criteria_view(request):
    result = None
    if request.method == 'POST':
        assignment_name = request.POST.get('assignment_name')
        criteria_file = request.FILES.get('criteria_file')

        if assignment_name and criteria_file:
            fastapi_url = f"http://fastapi:8001/assignments/{assignment_name}/criteria"
            files = {'criteria_file': (criteria_file.name, criteria_file.read(), criteria_file.content_type)}
            
            try:
                response = requests.post(fastapi_url, files=files, timeout=10)
                response.raise_for_status()
                result = json.dumps(response.json(), indent=4)
            except requests.RequestException as e:
                result = json.dumps({"error": str(e)}, indent=4)
        else:
            result = json.dumps({"error": "Assignment name and criteria file are required."}, indent=4)

    return render(request, 'upload_criteria.html', {'result': result})

def view_grades(request):
    fastapi_url = "http://fastapi:8001/grades"
    try:
        response = requests.get(fastapi_url, timeout=10)
        response.raise_for_status()
        results = response.json()
    except requests.RequestException as e:
        results = [{"error": str(e)}]
    
    # The results from the database will not have the assignment name, so we need to fetch it.
    # For now, we will just display the assignment id.
    # A better solution would be to join the tables in the backend.
    
    # The results from the database will not have the assignment name, so we need to fetch it.
    # I will modify the backend to include the assignment name in the response.
    
    return render(request, 'view_grades.html', {'results': results})
