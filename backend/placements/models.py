from django.db import models
class Student(models.Model):
 name = models.CharField(max_length=120)
 email = models.EmailField(unique=True)
 department = models.CharField(max_length=80, blank=True)
 graduation_year = models.PositiveSmallIntegerField(default=2027)
 created_at = models.DateTimeField(auto_now_add=True)
 class Meta: ordering = ['name']
 def __str__(self): return f'{self.name} ({self.email})'
class Recruiter(models.Model):
 company_name = models.CharField(max_length=160)
 contact_name = models.CharField(max_length=120)
 email = models.EmailField(unique=True)
 def __str__(self): return self.company_name
class Opportunity(models.Model):
 title = models.CharField(max_length=160)
 company = models.ForeignKey(Recruiter, on_delete=models.CASCADE, related_name='opportunities')
 description = models.TextField(blank=True)
 location = models.CharField(max_length=120, blank=True)
 deadline = models.DateField(null=True, blank=True, db_index=True)
 is_active = models.BooleanField(default=True, db_index=True)
 created_at = models.DateTimeField(auto_now_add=True)
 class Meta: ordering = ['-created_at']
 def __str__(self): return self.title
class Application(models.Model):
 class Status(models.TextChoices): APPLIED='APPLIED','Applied'; REVIEW='REVIEW','In review'; INTERVIEW='INTERVIEW','Interview'; OFFER='OFFER','Offer'; REJECTED='REJECTED','Rejected'
 student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='applications')
 opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE, related_name='applications')
 status = models.CharField(max_length=12, choices=Status.choices, default=Status.APPLIED, db_index=True)
 applied_at = models.DateTimeField(auto_now_add=True)
 class Meta:
  constraints = [models.UniqueConstraint(fields=['student','opportunity'], name='unique_student_opportunity')]
  ordering = ['-applied_at']
