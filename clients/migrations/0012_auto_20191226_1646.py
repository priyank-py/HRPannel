# Generated by Django 2.2.7 on 2019-12-26 11:16

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_auto_20191224_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetail',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True, verbose_name='Job description'),
        ),
    ]
