from django.urls import path
from .views import fetch_data_from_fastapi, submit_grading_request, upload_criteria_view, view_grades

urlpatterns = [
    path('fetch/', fetch_data_from_fastapi, name='fetch_data'),
    path('grade/', submit_grading_request, name='submit_grading_request'),
    path('upload-criteria/', upload_criteria_view, name='upload_criteria_view'),
    path('grades/', view_grades, name='view_grades'),
]
