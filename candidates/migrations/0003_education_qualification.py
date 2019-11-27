# Generated by Django 2.2.7 on 2019-11-27 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0002_hrremark'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='qualification',
            field=models.CharField(blank=True, choices=[('doctorate', 'Doctorate'), ('masters', 'masters'), ('bachelors', 'Bachelors'), ('high_school', 'High School/PUC')], max_length=50, null=True, verbose_name='Education level'),
        ),
    ]
