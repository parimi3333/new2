# Generated by Django 4.1.1 on 2022-09-16 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='employe',
        ),
        migrations.DeleteModel(
            name='profile',
        ),
    ]