from django.core.management.base import BaseCommand
from placements.models import Student, Recruiter, Opportunity
class Command(BaseCommand):
 help = 'Create a small local demo dataset (safe to run more than once).'
 def handle(self,*args,**kwargs):
  Student.objects.get_or_create(email='demo.student@example.com',defaults={'name':'Demo Student','department':'Computer Science','graduation_year':2027})
  recruiter,_=Recruiter.objects.get_or_create(email='talent@example.com',defaults={'company_name':'Northstar Labs','contact_name':'Campus Hiring'})
  Opportunity.objects.get_or_create(title='Software Engineering Intern',company=recruiter,defaults={'description':'Help build and test web services with a supportive engineering team.','location':'Bengaluru','is_active':True})
  self.stdout.write(self.style.SUCCESS('Demo data is ready.'))
