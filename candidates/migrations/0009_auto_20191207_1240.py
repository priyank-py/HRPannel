# Generated by Django 2.2.7 on 2019-12-07 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0008_auto_20191207_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrremark',
            name='reviewed_on',
            field=models.DateField(verbose_name='Reviewed on'),
        ),
    ]
