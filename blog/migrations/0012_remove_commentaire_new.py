# Generated by Django 2.2.6 on 2019-10-16 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20191016_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='new',
        ),
    ]
