# Generated by Django 2.2.7 on 2019-12-07 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20191207_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='commission',
            field=models.FloatField(blank=True, null=True, verbose_name='Commission Percentage'),
        ),
    ]
