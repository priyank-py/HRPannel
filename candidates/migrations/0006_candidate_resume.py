# Generated by Django 2.2.7 on 2019-12-03 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0005_auto_20191202_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='Resumes/%d-%b', verbose_name='Candidate Resume'),
        ),
    ]