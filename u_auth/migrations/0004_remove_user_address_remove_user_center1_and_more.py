# Generated by Django 4.1.1 on 2023-04-06 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("u_auth", "0003_rename_destrict_user_center1_user_center2"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="Address",
        ),
        migrations.RemoveField(
            model_name="user",
            name="Center1",
        ),
        migrations.RemoveField(
            model_name="user",
            name="Center2",
        ),
        migrations.RemoveField(
            model_name="user",
            name="Mobile",
        ),
        migrations.RemoveField(
            model_name="user",
            name="Mobile2",
        ),
    ]