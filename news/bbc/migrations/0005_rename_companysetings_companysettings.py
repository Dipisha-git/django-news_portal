# Generated by Django 4.0.2 on 2022-03-14 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bbc', '0004_companysetings_alter_news_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CompanySetings',
            new_name='CompanySettings',
        ),
    ]
