# Generated by Django 2.0 on 2018-11-03 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('read_statistics', '0004_auto_20181024_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='readnum',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType', verbose_name='类型'),
        ),
    ]
