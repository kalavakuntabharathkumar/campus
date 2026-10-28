import pytest
from django.test.utils import CaptureQueriesContext
from django.db import connection
from rest_framework.test import APIClient
from .models import Recruiter, Opportunity
@pytest.mark.django_db
def test_opportunities_endpoint_uses_select_related():
 recruiter=Recruiter.objects.create(company_name='Example Co',contact_name='Alex',email='alex@example.org')
 Opportunity.objects.create(title='QA Intern',company=recruiter)
 with CaptureQueriesContext(connection) as captured:
  response=APIClient().get('/api/opportunities/')
 assert response.status_code==200
 # The serializer accesses company_name; select_related should avoid one query per row.
 assert len(captured) <= 3
