# Generated by Django 4.1.7 on 2023-03-13 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0016_alter_registerbatch_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='isArchived',
            field=models.BooleanField(default=False),
        ),
    ]
