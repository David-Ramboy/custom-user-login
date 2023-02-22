# Generated by Django 4.1.6 on 2023-02-22 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='Ordered_Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proof_of_payment', models.ImageField(blank=True, null=True, upload_to='payment_images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_courses', to='course.category')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_courses', to='course.course')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_courses_price', to='course.course')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_courses', to='course.status')),
            ],
        ),
    ]
