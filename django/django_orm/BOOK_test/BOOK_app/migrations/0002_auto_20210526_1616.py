# Generated by Django 2.2.4 on 2021-05-26 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BOOK_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.AddField(
            model_name='author',
            name='first_name',
            field=models.CharField(default='jad', max_length=255),
        ),
        migrations.AddField(
            model_name='author',
            name='last_name',
            field=models.CharField(default='dawani', max_length=255),
        ),
    ]
