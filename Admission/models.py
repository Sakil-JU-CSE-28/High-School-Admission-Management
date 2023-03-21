from django.db import models

# Create your models here.
class applicant(models.Model):
    student_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    date_of_birth = models.DateTimeField()
    reg_no = models.IntegerField(primary_key=True)
    mobile = models.IntegerField()
