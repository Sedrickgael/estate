# Generated by Django 2.2.6 on 2019-10-17 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20191017_0257'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='email',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
