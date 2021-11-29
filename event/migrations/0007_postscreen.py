# Generated by Django 3.2.6 on 2021-09-27 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_auto_20210927_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostScreen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_screenshot', models.ImageField(default='prod_default_image.png', upload_to='event_icons/')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
        ),
    ]