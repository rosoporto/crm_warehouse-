# Generated by Django 5.1.2 on 2024-10-18 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("warehouse", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supplier",
            name="contact_person",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="email",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="phone",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
