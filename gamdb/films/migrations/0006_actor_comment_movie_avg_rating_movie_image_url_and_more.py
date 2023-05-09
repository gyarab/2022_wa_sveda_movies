# Generated by Django 4.1.7 on 2023-05-02 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0005_alter_movie_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birth_year', models.IntegerField(blank=True, null=True)),
                ('photo_url', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('rating', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='avg_rating',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(blank=True, null=True, to='films.genre'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]