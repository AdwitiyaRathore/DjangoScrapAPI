# Generated by Django 5.0.6 on 2024-06-07 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("scrapApp", "0002_marketdetail_coin_alter_marketdetail_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="marketdetail",
            name="detail",
        ),
    ]