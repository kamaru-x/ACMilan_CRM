# Generated by Django 4.1.1 on 2023-04-06 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Core", "0010_coordinator"),
    ]

    operations = [
        migrations.AddField(
            model_name="coordinator",
            name="Place",
            field=models.CharField(max_length=50, null=True),
        ),
    ]
