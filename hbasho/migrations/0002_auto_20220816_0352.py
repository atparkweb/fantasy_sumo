# Generated by Django 3.2.15 on 2022-08-16 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hbasho', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='stable',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_name'),
        ),
        migrations.AddConstraint(
            model_name='stable',
            constraint=models.UniqueConstraint(fields=('name_kanji',), name='unique_name_kanji'),
        ),
    ]
