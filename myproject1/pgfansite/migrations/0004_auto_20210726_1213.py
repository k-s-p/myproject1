# Generated by Django 3.2.5 on 2021-07-26 03:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pgfansite', '0003_alter_thread_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='updatedttm',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='thread',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
