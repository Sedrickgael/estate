# Generated by Django 2.2.6 on 2019-10-16 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20191016_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='new',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Article', to='blog.New'),
            preserve_default=False,
        ),
    ]
