# Generated by Django 3.2.5 on 2022-02-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20220226_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=models.TextField(default='Description', max_length=500),
        ),
    ]
