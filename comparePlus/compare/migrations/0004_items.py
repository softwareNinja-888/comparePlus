# Generated by Django 5.0.1 on 2024-07-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compare', '0003_rename_rating_stores_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64)),
                ('price', models.CharField(max_length=64)),
                ('image', models.ImageField(upload_to='')),
                ('rating', models.IntegerField()),
                ('storeWinner', models.CharField(blank=True, max_length=64)),
            ],
        ),
    ]