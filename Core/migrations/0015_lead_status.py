# Generated by Django 4.1.1 on 2023-04-06 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Core", "0014_lead_updates"),
    ]

    operations = [
        migrations.AddField(
            model_name="lead",
            name="Status",
            field=models.CharField(default="pending", max_length=10),
        ),
    ]
