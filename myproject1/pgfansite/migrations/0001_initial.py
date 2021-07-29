# Generated by Django 3.2.5 on 2021-07-26 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('published', models.DateTimeField()),
                ('image', models.ImageField(upload_to='media/')),
                ('username', models.CharField(max_length=20)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resno', models.IntegerField(default=0)),
                ('published', models.DateTimeField()),
                ('username', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pgfansite.thread')),
            ],
        ),
        migrations.AddConstraint(
            model_name='response',
            constraint=models.UniqueConstraint(fields=('thread', 'resno'), name='unique_stock'),
        ),
    ]