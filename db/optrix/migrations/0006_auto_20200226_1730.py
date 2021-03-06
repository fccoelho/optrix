# Generated by Django 3.0.3 on 2020-02-26 17:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('optrix', '0005_auto_20200213_1244'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='financial',
            options={'verbose_name_plural': 'Financial reports'},
        ),
        migrations.AlterModelOptions(
            name='postoperative',
            options={'verbose_name_plural': 'Postoperative reports'},
        ),
        migrations.AlterModelOptions(
            name='surgery',
            options={'ordering': ['date'], 'verbose_name_plural': 'Surgeries'},
        ),
        migrations.AlterField(
            model_name='patient',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 26, 17, 30, 57, 243212, tzinfo=utc), verbose_name='Date of admission'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
        migrations.AlterField(
            model_name='surgery',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 2, 26, 17, 30, 57, 243960, tzinfo=utc), verbose_name='Date of Surgery'),
        ),
        migrations.AlterField(
            model_name='surgery',
            name='robotic',
            field=models.BooleanField(default=False, help_text='Was the surgery robotic? <True|False>'),
        ),
    ]
