# Generated by Django 2.0 on 2018-09-12 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog1',
            options={'ordering': ['-created_time']},
        ),
    ]
