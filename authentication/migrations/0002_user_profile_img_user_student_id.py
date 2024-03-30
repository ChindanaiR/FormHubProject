# Generated by Django 5.0.3 on 2024-03-28 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='profile_img',
            field=models.ImageField(null=True, upload_to='static/userprofile/imgs'),
        ),
        migrations.AddField(
            model_name='user',
            name='student_id',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
