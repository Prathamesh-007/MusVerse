# Generated by Django 4.2.2 on 2023-07-09 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("new_app", "0002_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.CharField(max_length=70),
        ),
    ]
