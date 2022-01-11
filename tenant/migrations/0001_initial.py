# Generated by Django 3.1.5 on 2021-01-16 15:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('is_del', models.BooleanField(default=False, verbose_name='是否删除')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否可用')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=128)),
                ('slug', models.CharField(max_length=128)),
                ('use_slug', models.BooleanField(default=True, verbose_name='是否使用Slug')),
                ('background_url', models.URLField(blank=True, verbose_name='登录页背景图片')),
                ('copyright_text', models.CharField(max_length=512, blank=True, verbose_name='登录页版权文字')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
