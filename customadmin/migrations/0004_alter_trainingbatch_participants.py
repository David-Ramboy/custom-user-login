# Generated by Django 4.1.6 on 2023-03-01 04:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0011_registerbatch'),
        ('customadmin', '0003_alter_trainingbatch_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainingbatch',
            name='participants',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='training_batch', to='course.registerbatch'),
        ),
    ]