# Generated by Django 2.2.6 on 2019-10-16 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='nom',
        ),
        migrations.AddField(
            model_name='contact',
            name='contact',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='nom_complet',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
