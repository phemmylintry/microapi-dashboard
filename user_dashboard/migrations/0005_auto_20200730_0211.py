# Generated by Django 3.0.8 on 2020-07-30 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_dashboard', '0004_apilist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activeapilist',
            name='created_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='activeapilist',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
