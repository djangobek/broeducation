# Generated by Django 4.1.7 on 2023-03-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0008_alter_student_token_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="token_id",
            field=models.CharField(default="66420539", max_length=150),
        ),
    ]
