# Generated by Django 5.0.3 on 2024-03-29 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_management', '0003_alter_form_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='point',
            name='description',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
