# Generated by Django 4.0.4 on 2022-04-30 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songrecommender', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spotifyid', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='recommendation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]