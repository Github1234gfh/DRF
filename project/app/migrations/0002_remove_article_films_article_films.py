# Generated by Django 4.1.7 on 2023-03-14 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='films',
        ),
        migrations.AddField(
            model_name='article',
            name='films',
            field=models.ManyToManyField(to='app.films'),
        ),
    ]
