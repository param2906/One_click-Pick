# Generated by Django 4.1.7 on 2023-03-13 08:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0007_alter_products_colour_remove_products_size_size_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="products",
            name="size",
            field=models.ManyToManyField(max_length=5, to="products.size"),
        ),
    ]
