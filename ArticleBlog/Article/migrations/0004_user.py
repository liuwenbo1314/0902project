# Generated by Django 2.2.1 on 2019-11-11 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Article', '0003_auto_20191108_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
