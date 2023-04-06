# Generated by Django 4.1.1 on 2023-04-05 14:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("Core", "0006_students_reference"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="students",
            name="Adhar",
        ),
        migrations.RemoveField(
            model_name="students",
            name="Age_14_17",
        ),
        migrations.RemoveField(
            model_name="students",
            name="Age_4_13",
        ),
        migrations.RemoveField(
            model_name="students",
            name="Passport",
        ),
        migrations.AddField(
            model_name="students",
            name="Age_Group",
            field=models.CharField(default=django.utils.timezone.now, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="students",
            name="ID_Proof",
            field=models.CharField(default=django.utils.timezone.now, max_length=25),
            preserve_default=False,
        ),
    ]
