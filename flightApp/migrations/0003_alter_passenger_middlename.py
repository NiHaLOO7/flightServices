# Generated by Django 4.0.2 on 2022-03-03 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flightApp', '0002_alter_reservation_flight_alter_reservation_passenger'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='middleName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]