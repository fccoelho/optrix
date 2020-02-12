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

class Surgery(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    surgery_type = models.CharField(max_length=256)
    patient = models.ForeignKey('Patient', on_delete=models.deletion.DO_NOTHING)
    patient_in = models.TimeField(verbose_name='patient entered the operating room')
    patient_out = models.TimeField(verbose_name='Patient left the operating room')
    anesthetic_induction = models.CharField(max_length=512)
    robotic = models.BooleanField(default=False)
    incision_time = models.TimeField()
    suture_time = models.TimeField()
    estimated_blood_loss = models.FloatField(verbose_name='Blood loss in ml', default=0.0)
    transfusion = models.BooleanField(default=False)
    adverse_events = models.TextField(verbose_name="Adverse events during surgery")


