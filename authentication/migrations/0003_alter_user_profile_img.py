# Generated by Django 5.0.3 on 2024-04-18 08:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0002_user_profile_img_user_student_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="profile_img",
            field=models.ImageField(
                default="static/userprofile/imgs/default.jpg",
                null=True,
                upload_to="static/userprofile/imgs",
            ),
        ),
    ]
