# Generated by Django 5.0.1 on 2024-07-11 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0004_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='description',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
