# Generated by Django 2.2.1 on 2019-11-05 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0010_auto_20191105_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.IntegerField(verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(max_length=4, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='身高'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=32, verbose_name='姓名'),
        ),
    ]
