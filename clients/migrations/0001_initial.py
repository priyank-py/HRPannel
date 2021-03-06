# Generated by Django 2.2.7 on 2019-12-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Client Name')),
                ('address', models.TextField(verbose_name='Address')),
                ('company_type', models.CharField(choices=[('mnc', 'MNC'), ('sme', 'SME'), ('startup', 'Startup')], max_length=50, verbose_name='Company Type')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
