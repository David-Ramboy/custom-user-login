# Generated by Django 4.1.6 on 2023-02-23 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_remove_course_category_delete_category_delete_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='custom_user',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]