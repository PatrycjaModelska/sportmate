# Generated by Django 3.1.3 on 2020-11-21 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0003_auto_20201121_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sport',
            name='name',
            field=models.CharField(max_length=128, verbose_name='Nazwa sportu'),
        ),
    ]
