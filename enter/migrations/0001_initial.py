# Generated by Django 4.1.7 on 2023-03-07 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("ism_familya", models.CharField(max_length=200)),
                ("guruhi", models.CharField(max_length=200)),
                ("umumiy_bali", models.IntegerField()),
                (
                    "testda_ishtirok_etishi",
                    models.CharField(
                        choices=[("Passed", "O`tdi"), ("failed", "O`ta olmadi")],
                        default="O`tdi",
                        max_length=6,
                    ),
                ),
                (
                    "exam_day",
                    models.CharField(
                        choices=[
                            ("1", "kunlik imtihon"),
                            ("2", "haftalik imtihon"),
                            ("3", "Oylik Imtihon"),
                            ("4", "Yillik Imtihon"),
                        ],
                        default="Haftalik",
                        max_length=22,
                    ),
                ),
                ("exam_date", models.DateField()),
            ],
        ),
    ]