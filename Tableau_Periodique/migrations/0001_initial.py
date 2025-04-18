# Generated by Django 5.1.7 on 2025-04-17 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('symbole', models.CharField(max_length=5)),
                ('nom', models.CharField(max_length=50)),
                ('masse', models.CharField(max_length=20)),
                ('categorie', models.CharField(max_length=50)),
                ('position_row', models.IntegerField()),
                ('position_col', models.IntegerField()),
                ('atomic_radius', models.FloatField(blank=True, null=True)),
                ('electronegativity', models.FloatField(blank=True, null=True)),
                ('melting_point', models.FloatField(blank=True, null=True)),
            ],
        ),
    ]
