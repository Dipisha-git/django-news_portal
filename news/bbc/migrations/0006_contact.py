# Generated by Django 4.0.2 on 2022-03-16 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbc', '0005_rename_companysetings_companysettings'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=255)),
            ],
        ),
    ]
