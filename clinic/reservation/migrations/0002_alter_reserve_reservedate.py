# Generated by Django 4.0.3 on 2022-04-19 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserve',
            name='reservedate',
            field=models.DateField(default='date.today'),
        ),
    ]