# Generated by Django 4.0.5 on 2022-06-24 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_rename_osauhinguandmed_osauhinguandmedmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osauhinguandmedmodel',
            name='nimi',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='osauhinguandmedmodel',
            name='registrikood',
            field=models.CharField(max_length=7),
        ),
    ]
