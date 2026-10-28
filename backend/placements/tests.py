import pytest
from rest_framework.test import APIClient
from .models import Student, Recruiter, Opportunity, Application
@pytest.mark.django_db
def test_health_endpoint():
 response=APIClient().get('/api/health/')
 assert response.status_code==200 and response.json()['status']=='ok'
@pytest.mark.django_db
def test_students_create_and_list():
 client=APIClient()
 created=client.post('/api/students/', {'name':'Ananya Rao','email':'ananya@example.com','department':'CSE','graduation_year':2027}, format='json')
 assert created.status_code==201
 listing=client.get('/api/students/')
 assert listing.status_code==200
 data=listing.json(); assert data['count']==1 and data['results'][0]['name']=='Ananya Rao'
@pytest.mark.django_db
def test_duplicate_application_is_rejected():
 student=Student.objects.create(name='Dev',email='dev@example.com')
 recruiter=Recruiter.objects.create(company_name='Acme',contact_name='Riya',email='riya@acme.example')
 opportunity=Opportunity.objects.create(title='Backend Intern',company=recruiter)
 Application.objects.create(student=student,opportunity=opportunity)
 response=APIClient().post('/api/applications/',{'student':student.id,'opportunity':opportunity.id},format='json')
 assert response.status_code==400
