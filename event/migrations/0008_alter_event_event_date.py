# Generated by Django 3.2.6 on 2021-09-27 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_postscreen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(),
        ),
    ]
