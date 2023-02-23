# Generated by Django 4.1.6 on 2023-02-23 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0009_alter_ordered_course_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('proof_of_payment', models.ImageField(upload_to='payment_images/')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('processing', 'Processing'), ('paid', 'Paid'), ('cancelled', 'Cancelled'), ('completed', 'Completed')], default='pending', max_length=20)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_courses', to='course.course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Ordered_Course',
        ),
    ]
