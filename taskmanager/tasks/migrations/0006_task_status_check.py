# Generated by Django 4.2.2 on 2024-01-30 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0005_sprint_end_date_after_start_date"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="task",
            constraint=models.CheckConstraint(
                check=models.Q(
                    ("status", "UNASSIGNED"),
                    ("status", "IN_PROGRESS"),
                    ("status", "DONE"),
                    ("status", "ARCHIVED"),
                    _connector="OR",
                ),
                name="status_check",
            ),
        ),
    ]
