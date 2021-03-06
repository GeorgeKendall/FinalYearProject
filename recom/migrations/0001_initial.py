# Generated by Django 3.2.5 on 2022-04-22 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_path', models.URLField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('genre', models.CharField(max_length=255)),
                ('overview', models.TextField()),
                ('director', models.CharField(max_length=255)),
                ('s1', models.CharField(max_length=255)),
                ('s2', models.CharField(max_length=255)),
                ('s3', models.CharField(max_length=255)),
                ('s4', models.CharField(max_length=255)),
                ('soup', models.TextField()),
            ],
        ),
    ]
