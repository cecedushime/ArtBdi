# Generated by Django 5.0.4 on 2024-05-09 10:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_art', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.RenameField(
            model_name='artistes',
            old_name='id_artiste',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='clients',
            old_name='id_client',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='oeuvre_art',
            old_name='id_oeuvre',
            new_name='id',
        ),
        migrations.RemoveField(
            model_name='artistes',
            name='biographie',
        ),
        migrations.RemoveField(
            model_name='clients',
            name='prenom',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='id_reservation',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='status',
        ),
        migrations.AddField(
            model_name='artistes',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='artistes',
            name='visible',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='clients',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='oeuvre_art',
            name='artistes',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_art.artistes'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='client',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app_art.clients'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='oeuvre_art',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app_art.oeuvre_art'),
        ),
        migrations.AlterField(
            model_name='artistes',
            name='contact',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='artistes',
            name='pseudounymes',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='oeuvre_art',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_debut', models.DateTimeField()),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_art.reservation')),
            ],
        ),
        migrations.CreateModel(
            name='Panier',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantite', models.PositiveIntegerField(default=1)),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app_art.clients')),
                ('oeuvre_art', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app_art.oeuvre_art')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantite_initiale', models.FloatField(default=0)),
                ('quantite_actuelle', models.FloatField(editable=False, null=True)),
                ('oeuvre_art', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app_art.oeuvre_art')),
            ],
        ),
    ]