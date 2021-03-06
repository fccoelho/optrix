# Generated by Django 3.0.3 on 2020-03-09 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('optrix', '0007_auto_20200301_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Surgeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64)),
                ('CRM', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='surgery',
            name='hospital',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='optrix.Hospital'),
        ),
        migrations.AddField(
            model_name='surgery',
            name='surgeon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='optrix.Surgeon'),
        ),
    ]
