# Generated by Django 3.2.6 on 2021-09-28 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0009_auto_20210928_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_doc_link',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=2),
        ),
    ]
