# Generated by Django 4.1.3 on 2022-12-21 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_wilayahdbapi"),
    ]

    operations = [
        migrations.CreateModel(
            name="KotaAPI",
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
                ("id_kota", models.CharField(blank=True, max_length=200, null=True)),
                ("kota", models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="ProvAPI",
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
                ("id_prov", models.CharField(blank=True, max_length=200, null=True)),
                ("prov", models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name="WilayahDBAPI",
        ),
    ]