from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student, Recruiter, Opportunity, Application
from .serializers import StudentSerializer, RecruiterSerializer, OpportunitySerializer, ApplicationSerializer
@api_view(['GET'])
def health(request): return Response({'status':'ok','service':'campusconnect'})
class StudentViewSet(viewsets.ModelViewSet):
 queryset=Student.objects.all().order_by('name'); serializer_class=StudentSerializer; search_fields=['name','email','department']; filter_backends=[filters.SearchFilter]
class RecruiterViewSet(viewsets.ModelViewSet): queryset=Recruiter.objects.all(); serializer_class=RecruiterSerializer
class OpportunityViewSet(viewsets.ModelViewSet):
 queryset=Opportunity.objects.select_related('company').filter(is_active=True); serializer_class=OpportunitySerializer; search_fields=['title','company__company_name','location']; filter_backends=[filters.SearchFilter]
class ApplicationViewSet(viewsets.ModelViewSet):
 queryset=Application.objects.select_related('student','opportunity').all(); serializer_class=ApplicationSerializer; filterset_fields=['status','student','opportunity']
