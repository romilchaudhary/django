# Generated by Django 4.1.1 on 2022-09-22 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_customuser_user_alter_customuser_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='abc.png', upload_to='profile/pics'),
        ),
    ]