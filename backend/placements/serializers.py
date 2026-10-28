from rest_framework import serializers
from .models import Student, Recruiter, Opportunity, Application
class StudentSerializer(serializers.ModelSerializer):
 class Meta: model=Student; fields='__all__'; read_only_fields=['id','created_at']
class RecruiterSerializer(serializers.ModelSerializer):
 class Meta: model=Recruiter; fields='__all__'; read_only_fields=['id']
class OpportunitySerializer(serializers.ModelSerializer):
 company_name = serializers.CharField(source='company.company_name', read_only=True)
 class Meta: model=Opportunity; fields=['id','title','company','company_name','description','location','deadline','is_active','created_at']; read_only_fields=['id','created_at']
class ApplicationSerializer(serializers.ModelSerializer):
 student_name = serializers.CharField(source='student.name', read_only=True)
 opportunity_title = serializers.CharField(source='opportunity.title', read_only=True)
 class Meta: model=Application; fields=['id','student','student_name','opportunity','opportunity_title','status','applied_at']; read_only_fields=['id','applied_at']
