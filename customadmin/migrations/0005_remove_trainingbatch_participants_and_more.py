# Generated by Django 4.1.6 on 2023-03-01 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_registerbatch'),
        ('customadmin', '0004_alter_trainingbatch_participants'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainingbatch',
            name='participants',
        ),
        migrations.AddField(
            model_name='trainingbatch',
            name='participants',
            field=models.ManyToManyField(to='course.registerbatch'),
        ),
    ]
