# Generated by Django 4.1.1 on 2023-04-06 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Core", "0011_coordinator_place"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lead",
            name="Coordinator",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="Core.coordinator"
            ),
        ),
    ]
