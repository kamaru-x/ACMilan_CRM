# Generated by Django 4.1.1 on 2023-04-06 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Core", "0008_center"),
    ]

    operations = [
        migrations.AddField(
            model_name="center",
            name="Students",
            field=models.IntegerField(default=0),
        ),
    ]
