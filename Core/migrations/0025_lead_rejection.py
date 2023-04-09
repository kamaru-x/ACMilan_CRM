# Generated by Django 4.1.1 on 2023-04-09 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Core", "0024_center_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Lead_Rejection",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Date", models.DateField(auto_now_add=True)),
                ("Reason", models.TextField()),
                (
                    "Lead",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING, to="Core.lead"
                    ),
                ),
            ],
        ),
    ]