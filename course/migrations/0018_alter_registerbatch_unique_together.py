# Generated by Django 4.1.7 on 2023-03-14 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0017_course_isarchived'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registerbatch',
            unique_together=set(),
        ),
    ]
