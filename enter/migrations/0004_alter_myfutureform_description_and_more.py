# Generated by Django 4.1.7 on 2023-03-09 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("enter", "0003_myfutureform"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myfutureform",
            name="description",
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name="myfutureform",
            name="full_name",
            field=models.CharField(max_length=400),
        ),
    ]
