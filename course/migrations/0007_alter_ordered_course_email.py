# Generated by Django 4.1.6 on 2023-02-22 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_alter_ordered_course_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordered_course',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
