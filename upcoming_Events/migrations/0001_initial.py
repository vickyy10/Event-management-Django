# Generated by Django 5.0.6 on 2024-07-05 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UpcomingEvents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_name', models.CharField(max_length=50)),
                ('loaction', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('image', models.ImageField(upload_to='')),
                ('ticket_availability', models.BigIntegerField()),
                ('ticket_price', models.BigIntegerField()),
                ('peoplestrength', models.BigIntegerField()),
            ],
        ),
    ]
