# Generated by Django 2.2.6 on 2019-10-15 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSlide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/team/about/')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'AboutSlide',
                'verbose_name_plural': 'AboutSlides',
            },
        ),
        migrations.CreateModel(
            name='APropos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_entreprise', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('experience', models.PositiveIntegerField()),
                ('join_team_message', models.TextField()),
                ('work_remote', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'APropos',
                'verbose_name_plural': 'AProposs',
            },
        ),
        migrations.CreateModel(
            name='Poste',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
        ),
        migrations.CreateModel(
            name='Membre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenoms', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('contact', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=255)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('bureau', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bureau', to='config.Bureau')),
                ('poste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poste', to='team.Poste')),
            ],
            options={
                'verbose_name': 'Membre',
                'verbose_name_plural': 'Membres',
            },
        ),
    ]
