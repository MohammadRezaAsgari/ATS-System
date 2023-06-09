# Generated by Django 4.0.6 on 2022-08-30 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicant_tracking_system', '0004_telegrambot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='gender',
            field=models.TextField(choices=[('none', 'none'), ('male', 'male'), ('female', 'female')], default='n', max_length=6),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='status',
            field=models.TextField(choices=[('pending', 'pending'), ('inProgress', 'inProgress'), ('accepted', 'accepted'), ('failed', 'failed')], default='p', max_length=10),
        ),
    ]
