# Generated by Django 3.1.3 on 2020-11-18 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='Name',
            field=models.CharField(default='N/A', max_length=200),
        ),
    ]
