# Generated by Django 4.1.7 on 2023-03-22 10:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="status",
        ),
        migrations.AddField(
            model_name="orderitem",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Out for delivary", "Out for delivary"),
                    ("Delivered", "Delivered"),
                ],
                max_length=200,
                null=True,
            ),
        ),
    ]
