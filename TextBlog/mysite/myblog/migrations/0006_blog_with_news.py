# Generated by Django 2.0 on 2018-10-13 07:53

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myblog', '0005_auto_20181013_1235'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog_with_news',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='标题')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='内容')),
                ('reader_num', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='修改时间')),
                ('last_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('blog_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myblog.BlogType', verbose_name='类型')),
            ],
        ),
    ]