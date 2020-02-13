from django.db import models
import django


class Patient(models.Model):
    date = models.DateField(verbose_name='Date of admission', default=django.utils.timezone.now())
    number = models.IntegerField(verbose_name='Patient number')
    crypto_key = models.CharField(verbose_name="Patient key", max_length=100, null=False)
    sex = models.CharField(max_length=1)  # , choices=[('M', 'Male', 'F', 'Female')])
    age = models.IntegerField()
    weight = models.FloatField()
    diagnosis = models.CharField(verbose_name='Disease code (ICD-10)', max_length=16)
    asa_grade = models.FloatField(verbose_name='ASA grade')

    def __str__(self):
        return f"Patient {self.number}, admitted on: {self.date}"


class Surgery(models.Model):
    surgery_type = models.CharField(max_length=256)
    date = models.DateField(verbose_name='Date of Surgery', default=django.utils.timezone.now())
    patient = models.ForeignKey('Patient', on_delete=models.deletion.DO_NOTHING)
    patient_in = models.TimeField(verbose_name='patient entered the operating room')
    patient_out = models.TimeField(verbose_name='Patient left the operating room')
    anesthetic_induction = models.CharField(max_length=512)
    robotic = models.BooleanField(default=False)
    incision_time = models.TimeField()
    suture_time = models.TimeField()
    estimated_blood_loss = models.FloatField(verbose_name='Blood loss in ml', default=0.0)
    transfusion = models.BooleanField(default=False)
    conversion_to_lap_open = models.BooleanField(verbose_name='Converted to Lap./Open surgery', default=False)
    instruments_used = models.TextField(verbose_name='Instruments used')
    adverse_events = models.TextField(verbose_name="Adverse events during surgery")

    def __str__(self):
        return f"{self.surgery_type} on {self.date}"

    class Meta:
        ordering = ['date']
        verbose_name_plural = "Surgeries"


class Postoperative(models.Model):
    surgery = models.ForeignKey('Surgery', on_delete=models.deletion.CASCADE)
    robotic_or_cleaning = models.BooleanField(verbose_name='Robotic OR cleaning', default=False)
    returned_to_or = models.BooleanField(verbose_name='Returned to OR before discharge', default=False)
    expected_discharge_date = models.DateField(verbose_name='Expected date of discharge')
    actual_discharge_date = models.DateField(verbose_name='Actual date of discharge')
    return_to_hospital = models.BooleanField(verbose_name='Readmitted to Hospital withing 30 days')
    death_90 = models.BooleanField(verbose_name='Death within 90 days', default=False)
    complications = models.TextField(verbose_name='Complications description')

    class Meta:
        verbose_name_plural = "Postoperative reports"


class Financial(models.Model):
    surgery = models.ForeignKey('Surgery', on_delete=models.deletion.CASCADE)
    materials_cost = models.FloatField(verbose_name='Cost of materials (consumables and instruments)')
    medication_cost = models.FloatField(verbose_name='Cost of medication')
    surgical_team = models.FloatField(verbose_name='Cost of surgical team')
    other_costs = models.FloatField(verbose_name='Other personnel costs (nurses, etc.)')
    or_time_cost = models.FloatField(verbose_name='Operating Room time cost')
    icu_cost = models.FloatField(verbose_name='ICU cost')
    robotic_cost = models.FloatField(verbose_name='Robotic system cost')
    robot_maint_cost = models.FloatField(verbose_name='Robot maintenance fee')
    sterilization_cost = models.FloatField(verbose_name='Sterilization cost')

    class Meta:
        verbose_name_plural = "Financial reports"
