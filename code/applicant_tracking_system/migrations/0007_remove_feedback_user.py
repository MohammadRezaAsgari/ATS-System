# Generated by Django 4.0.6 on 2022-09-10 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('applicant_tracking_system', '0006_alter_interview_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='user',
        ),
    ]
