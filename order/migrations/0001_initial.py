# Generated by Django 4.1.7 on 2023-03-22 06:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0010_products_inventory"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("first_name", models.CharField(max_length=50, null=True)),
                ("last_name", models.CharField(max_length=50, null=True)),
                ("phone", models.CharField(blank=True, max_length=10, null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("address1", models.CharField(blank=True, max_length=20, null=True)),
                ("address2", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "total_price",
                    models.DecimalField(decimal_places=2, max_digits=10, null=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Pending", "Pending"),
                            ("Out for deleivery", "Out for delivery"),
                            ("Delivered", "Delivered"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user.order.created_by+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "update_by",
                    models.ForeignKey(
                        blank=True,
                        max_length=200,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user.order.updated_by+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user.order+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("size", models.CharField(blank=True, max_length=5, null=True)),
                ("colour", models.CharField(blank=True, max_length=20, null=True)),
                ("quantity", models.IntegerField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user.orderitem.created_by+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="order+",
                        to="order.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="orderitem+",
                        to="products.products",
                    ),
                ),
                (
                    "update_by",
                    models.ForeignKey(
                        blank=True,
                        max_length=200,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="user.orderitem.updated_by+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
