# Generated by Django 2.2.6 on 2019-10-16 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20191016_0103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auteur',
            name='avatar',
        ),
    ]
