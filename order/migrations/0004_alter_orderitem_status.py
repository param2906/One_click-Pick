# Generated by Django 4.1.7 on 2023-03-22 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0003_alter_orderitem_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orderitem",
            name="status",
            field=models.CharField(
                choices=[
                    ("25", "Pending"),
                    ("70", "Out for delivary"),
                    ("100", "Delivered"),
                ],
                max_length=200,
                null=True,
            ),
        ),
    ]
