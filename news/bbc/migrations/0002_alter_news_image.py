# Generated by Django 4.0.2 on 2022-03-03 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='bbc'),
        ),
    ]
