# Generated by Django 2.2.6 on 2019-10-16 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_auteur_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newimage',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.New', verbose_name='article'),
        ),
    ]
