# Generated by Django 4.1.1 on 2022-10-01 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('eid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=70)),
                ('mfdt', models.DateField()),
                ('expdt', models.DateField()),
            ],
        ),
    ]