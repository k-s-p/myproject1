# Generated by Django 3.2.5 on 2021-07-28 14:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pgfansite', '0005_thread_response_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
