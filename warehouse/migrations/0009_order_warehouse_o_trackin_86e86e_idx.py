# Generated by Django 5.1.2 on 2024-10-25 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("warehouse", "0008_order_tracking_number"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                fields=["tracking_number"], name="warehouse_o_trackin_86e86e_idx"
            ),
        ),
    ]