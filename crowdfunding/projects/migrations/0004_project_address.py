# Generated by Django 4.1.5 on 2023-01-21 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0003_alter_pledge_supporter_alter_project_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="address",
            field=models.CharField(blank=True, default="", max_length=200),
        ),
    ]
