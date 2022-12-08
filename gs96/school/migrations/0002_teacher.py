# Generated by Django 4.1.2 on 2022-11-29 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("school", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                ("name", models.CharField(max_length=20)),
                ("empnum", models.IntegerField(unique=True)),
                ("city", models.CharField(max_length=20)),
                ("salary", models.IntegerField()),
                ("join_date", models.DateField()),
            ],
        ),
    ]
