# Generated by Django 2.2.7 on 2019-12-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_jobdetail_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdetail',
            name='job_type',
            field=models.CharField(blank=True, choices=[('fulltime', 'Full-Time'), ('parttime', 'Part-Time'), ('contract', 'Contract'), ('internship', 'Internship')], max_length=50, null=True, verbose_name='Type'),
        ),
    ]