# Generated by Django 4.2 on 2023-05-10 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("rufus_app", "0011_alter_dishitem_name_alter_dishitem_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menu",
            name="name",
        ),
    ]
