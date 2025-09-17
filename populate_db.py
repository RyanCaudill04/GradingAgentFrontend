import os
import django
import uuid
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')
django.setup()

from AgentDeployer.models import Submission

def populate():
    # Clear existing data
    Submission.objects.all().delete()

    # Create new data
    submission1 = Submission.objects.create(
        submission_id=uuid.uuid4(),
        student_name='Alice',
        assignment_name='Assignment 1',
        repo_link='http://github.com/alice/repo',
        token='alice_token',
        submission_time=datetime.now(),
        status='COMPLETED',
        fastapi_response={
            'final_grade': 95,
            'deductions': [
                {'reason': 'Late submission', 'points': 5}
            ]
        }
    )

    submission2 = Submission.objects.create(
        submission_id=uuid.uuid4(),
        student_name='Bob',
        assignment_name='Assignment 1',
        repo_link='http://github.com/bob/repo',
        token='bob_token',
        submission_time=datetime.now(),
        status='COMPLETED',
        fastapi_response={
            'final_grade': 80,
            'deductions': [
                {'reason': 'Missing file', 'points': 10},
                {'reason': 'Incorrect output', 'points': 10}
            ]
        }
    )

    submission3 = Submission.objects.create(
        submission_id=uuid.uuid4(),
        student_name='Charlie',
        assignment_name='Assignment 2',
        repo_link='http://github.com/charlie/repo',
        token='charlie_token',
        submission_time=datetime.now(),
        status='COMPLETED',
        fastapi_response={
            'final_grade': 100,
            'deductions': []
        }
    )

    print('Database populated with sample data.')

if __name__ == '__main__':
    populate()
