# Generated by Django 2.1.9 on 2019-06-11 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactsubmission',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]
