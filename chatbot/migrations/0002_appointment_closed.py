# Generated by Django 4.0 on 2024-07-11 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='closed',
            field=models.BooleanField(default=False),
        ),
    ]
