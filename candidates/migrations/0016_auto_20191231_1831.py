# Generated by Django 2.2.7 on 2019-12-31 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0015_auto_20191228_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hrremark',
            name='considered_for',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='clients.JobDetail', verbose_name='Considered for'),
        ),
    ]
