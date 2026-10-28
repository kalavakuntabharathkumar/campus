from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(name='Recruiter', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('company_name', models.CharField(max_length=160)), ('contact_name', models.CharField(max_length=120)), ('email', models.EmailField(max_length=254, unique=True))]),
        migrations.CreateModel(name='Student', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('name', models.CharField(max_length=120)), ('email', models.EmailField(max_length=254, unique=True)), ('department', models.CharField(blank=True, max_length=80)), ('graduation_year', models.PositiveSmallIntegerField(default=2027)), ('created_at', models.DateTimeField(auto_now_add=True))], options={'ordering': ['name']}),
        migrations.CreateModel(name='Opportunity', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('title', models.CharField(max_length=160)), ('description', models.TextField(blank=True)), ('location', models.CharField(blank=True, max_length=120)), ('deadline', models.DateField(blank=True, db_index=True, null=True)), ('is_active', models.BooleanField(db_index=True, default=True)), ('created_at', models.DateTimeField(auto_now_add=True)), ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opportunities', to='placements.recruiter'))], options={'ordering': ['-created_at']}),
        migrations.CreateModel(name='Application', fields=[('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')), ('status', models.CharField(choices=[('APPLIED', 'Applied'), ('REVIEW', 'In review'), ('INTERVIEW', 'Interview'), ('OFFER', 'Offer'), ('REJECTED', 'Rejected')], db_index=True, default='APPLIED', max_length=12)), ('applied_at', models.DateTimeField(auto_now_add=True)), ('opportunity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='placements.opportunity')), ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='placements.student'))], options={'ordering': ['-applied_at']}),
        migrations.AddConstraint(model_name='application', constraint=models.UniqueConstraint(fields=('student', 'opportunity'), name='unique_student_opportunity')),
    ]
