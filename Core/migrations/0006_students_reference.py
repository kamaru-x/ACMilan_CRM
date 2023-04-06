# Generated by Django 4.1.1 on 2023-04-05 11:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("Core", "0005_students"),
    ]

    operations = [
        migrations.AddField(
            model_name="students",
            name="Reference",
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
    ]