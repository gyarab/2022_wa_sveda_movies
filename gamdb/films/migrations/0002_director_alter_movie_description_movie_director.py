# Generated by Django 4.1.7 on 2023-03-21 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birth_year', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='films.director'),
        ),
    ]
