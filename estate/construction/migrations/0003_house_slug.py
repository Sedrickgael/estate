# Generated by Django 2.2.6 on 2019-10-16 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0002_auto_20191016_0833'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
