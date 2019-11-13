# Generated by Django 2.2.1 on 2019-11-13 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=32)),
                ('username', models.CharField(max_length=32)),
                ('phone_number', models.CharField(blank=True, max_length=32, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('gender', models.IntegerField(choices=[(0, '女'), (1, '男')])),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 'loginuser',
            },
        ),
    ]
