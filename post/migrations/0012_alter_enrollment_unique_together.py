# Generated by Django 4.1.1 on 2022-09-23 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_alter_enrollment_final_grade'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('course', 'student')},
        ),
    ]
