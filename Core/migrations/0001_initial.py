# Generated by Django 4.1.1 on 2023-04-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Lead",
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
                ("Reference", models.CharField(max_length=15)),
                ("Student_Name", models.CharField(max_length=50)),
                ("Gardian_Name", models.CharField(max_length=50)),
                ("Contact_Number", models.CharField(max_length=15)),
                ("Contact_Date", models.DateField(auto_now_add=True)),
            ],
        ),
    ]