# Generated by Django 4.0.3 on 2022-04-19 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_reserve_reservedate'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserve',
            name='docName',
            field=models.CharField(default='Amirreza Hosseini', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reserve',
            name='reservetime',
            field=models.TimeField(default='23:59'),
            preserve_default=False,
        ),
    ]
