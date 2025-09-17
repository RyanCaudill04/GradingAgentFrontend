from django.urls import path
from .views import home, fetch_data_from_fastapi, submit_grading_request, upload_criteria_view, view_grades, submission_list, submission_detail

urlpatterns = [
    path('', home, name='home'),
    path('fetch/', fetch_data_from_fastapi, name='fetch_data'),
    path('grade/', submit_grading_request, name='submit_grading_request'),
    path('upload-criteria/', upload_criteria_view, name='upload_criteria'),
    path('grades/', view_grades, name='view_grades'),
    path('submissions/', submission_list, name='submission_list'),
    path('submissions/<uuid:submission_id>/', submission_detail, name='submission_detail'),
]
