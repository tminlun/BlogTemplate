# Generated by Django 2.0 on 2018-10-11 12:17

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20181011_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='blog_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myblog.BlogType', verbose_name='类型'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='修改时间'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='last_time',
            field=models.DateTimeField(auto_now=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=20, verbose_name='标题'),
        ),
        migrations.AlterField(
            model_name='blogtype',
            name='type_name',
            field=models.CharField(max_length=15, verbose_name='类型名称'),
        ),
    ]
