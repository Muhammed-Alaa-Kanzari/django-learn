# Generated by Django 5.0.6 on 2024-07-29 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='International Standard Book Number'),
        ),
    ]
