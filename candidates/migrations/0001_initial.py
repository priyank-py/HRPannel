# Generated by Django 2.2.7 on 2019-11-19 09:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('dob', models.DateField(verbose_name='Date of Birth')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=50, verbose_name='Phone No.')),
                ('alternate_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Alternate No.')),
                ('location', models.CharField(max_length=50, verbose_name='Location')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=50, verbose_name='Gender')),
            ],
            options={
                'verbose_name': 'Candidate',
                'verbose_name_plural': 'Candidates',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Skill')),
                ('experience', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Experience (in Years)')),
                ('last_used', models.IntegerField(blank=True, choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], null=True, verbose_name='till')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='candidates.Candidate', verbose_name='Candidates')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50, verbose_name='Company Name')),
                ('job_profile', models.CharField(max_length=50, verbose_name='Job Profile')),
                ('current_company', models.BooleanField(blank=True, choices=[(True, 'Yes'), (False, 'No')], null=True, verbose_name='Is this you current company?')),
                ('start', models.DateField(blank=True, null=True, verbose_name='Started on')),
                ('end', models.DateField(blank=True, null=True, verbose_name='Worked Till')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='candidates.Candidate', verbose_name='Candidate')),
            ],
            options={
                'verbose_name': 'Experience',
                'verbose_name_plural': 'Experiences',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=80, verbose_name='Degree Qualified')),
                ('start', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], verbose_name='From')),
                ('end', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019)], verbose_name='till')),
                ('college_name', models.CharField(max_length=80, verbose_name='College Name')),
                ('marks', models.FloatField(validators=[django.core.validators.MinValueValidator(39.99), django.core.validators.MaxValueValidator(100)], verbose_name='Marks Obtained')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='candidates.Candidate', verbose_name='Candidate')),
            ],
            options={
                'verbose_name': 'Education',
                'verbose_name_plural': 'Educations',
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Certification Name')),
                ('organisation', models.CharField(max_length=50, verbose_name='Issuing Organisation')),
                ('issue', models.DateField(blank=True, null=True, verbose_name='Issue Date')),
                ('expire', models.DateField(blank=True, null=True, verbose_name='Expiration Date')),
                ('certificate_id', models.CharField(blank=True, max_length=50, null=True, verbose_name='Credential ID')),
                ('certificate_url', models.URLField(blank=True, null=True, verbose_name='Credential URL')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='certificates', to='candidates.Candidate', verbose_name='Candidate')),
            ],
            options={
                'verbose_name': 'Certificate',
                'verbose_name_plural': 'Certificates',
            },
        ),
    ]