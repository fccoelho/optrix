from django.db import models


class Patient(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    date = models.DateField(verbose_name='Date of surgery', auto_now_add=True)
    number = models.IntegerField(verbose_name='Patient number')
    crypto_key = models.CharField(verbose_name="Patient key", max_length=100, null=False)
    sex = models.CharField(max_length=1)#, choices=[('M', 'Male', 'F', 'Female')])
    age = models.IntegerField()
    weight = models.FloatField()
    diagnosis = models.CharField(verbose_name='Disease code (ICD-10)', max_length=16)
    asa_grade = models.FloatField(verbose_name='ASA grade')
