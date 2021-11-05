# Generated by Django 3.2.8 on 2021-11-05 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_sync', '0002_datasyncconfig_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasyncconfig',
            name='sync_mode',
            field=models.CharField(choices=[('client', 'Client mode'), ('server', 'Server mode')], default='server', max_length=32, verbose_name='同步模式'),
        ),
    ]
