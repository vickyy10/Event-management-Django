# Generated by Django 5.0.6 on 2024-07-10 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upcoming_Events', '0007_upcomingeventsbooking_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='upcomingeventsbooked',
            name='numberoftickets',
        ),
    ]
