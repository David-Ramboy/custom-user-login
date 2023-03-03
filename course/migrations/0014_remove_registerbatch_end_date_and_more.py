# Generated by Django 4.1.7 on 2023-03-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_registerbatch_end_date_registerbatch_start_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerbatch',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='registerbatch',
            name='start_date',
        ),
        migrations.AddField(
            model_name='registerbatch',
            name='batch_course_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
