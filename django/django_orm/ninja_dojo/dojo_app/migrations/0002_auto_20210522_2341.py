# Generated by Django 2.2.4 on 2021-05-22 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ninja',
            old_name='name',
            new_name='last_name',
        ),
        migrations.AddField(
            model_name='ninja',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
