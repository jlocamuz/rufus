# Generated by Django 4.2 on 2023-05-05 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rufus_app', '0009_alter_dishitem_pictogram_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishitem',
            name='pictogram_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
