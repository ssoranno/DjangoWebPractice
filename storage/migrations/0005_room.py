# Generated by Django 3.1.3 on 2020-12-04 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0004_auto_20201117_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('FloorNumber', models.IntegerField()),
                ('RoomNumber', models.IntegerField()),
            ],
        ),
    ]
