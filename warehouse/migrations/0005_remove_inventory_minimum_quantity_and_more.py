# Generated by Django 5.1.2 on 2024-10-18 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("warehouse", "0004_alter_order_comments"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="inventory",
            name="minimum_quantity",
        ),
        migrations.RemoveField(
            model_name="product",
            name="quantity",
        ),
        migrations.AlterField(
            model_name="inventory",
            name="quantity",
            field=models.IntegerField(default=0),
        ),
    ]