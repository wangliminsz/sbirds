# Generated by Django 3.2.5 on 2021-07-16 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fbot_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='poempoem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poemid', models.IntegerField()),
                ('poemen1', models.TextField()),
                ('poemen2', models.TextField()),
                ('poemen3', models.TextField()),
                ('poemen4', models.TextField()),
                ('poemcn1', models.TextField()),
                ('poemcn2', models.TextField()),
                ('poemcn3', models.TextField()),
                ('poemcn4', models.TextField()),
            ],
        ),
    ]
