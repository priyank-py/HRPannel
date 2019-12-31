from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _ 
from taggit.managers import TaggableManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import get_object_or_404
from tinymce.models import HTMLField

# Create your models here.
class Client(models.Model):

    COMPANY_TYPES =     (
        ('mnc', 'MNC'),
        ('sme', 'SME'),
        ('startup', 'Startup'),
    )

    name = models.CharField(_("Client Name"), max_length=50)
    address = models.TextField(_("Address"))
    company_type = models.CharField(_("Company Type"), max_length=50, choices=COMPANY_TYPES)

    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("each_client", kwargs={"pk": self.pk})


class ContactPerson(models.Model):
    client = models.ForeignKey(Client, verbose_name=_("client"), related_name="client_cp", on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(_("Name"), max_length=50)
    designation = models.CharField(_("Designation"), max_length=50)
    contact_no = models.CharField(_("Contact No."), max_length=50)
    alternate_no = models.CharField(_("Alternate No."), max_length=50, blank=True, null=True)
    email = models.EmailField(_("Email ID"), max_length=254)
    
    class Meta:
        verbose_name = _("ContactPerson")
        verbose_name_plural = _("ContactPersons")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ContactPerson_detail", kwargs={"pk": self.pk})

class Agreement(models.Model):
    AGREEMENT_STATUS = (
        ('signed', 'Signed'),
        ('unsigned', 'Unsigned'),
    )
    client = models.ForeignKey(Client, verbose_name=_("client"), related_name="client_agreement", on_delete=models.CASCADE, blank=True, null=True)
    agreement = models.FileField(_("Agreement Copy"), upload_to='Agreements/%d-%m-%Y', max_length=100, blank=True, null=True)
    agreement_status = models.CharField(_("Agreement Status"), max_length=50, choices=AGREEMENT_STATUS)
    start_date = models.DateField(_("Start Date"), auto_now=False, auto_now_add=False)
    end_date = models.DateField(_("End Date"), auto_now=False, auto_now_add=False)
    commission = models.FloatField(_("Commission Percentage"), blank=True, null=True)
    
    def __str__(self):
        return f'{self.client.name.capitalize()} Ag.({self.start_date} - {self.end_date})'
     

    class Meta:
        verbose_name = _("Agreement")
        verbose_name_plural = _("Agreements")



class JobDetail(models.Model):

    TYPE_CHOICES = (
        ('fulltime', 'Full-Time'),
        ('parttime', 'Part-Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    )

    agreement = models.ForeignKey(Agreement, verbose_name=_("agreement"), related_name="job_agreement", on_delete=models.CASCADE, blank=True, null=True)
    client = models.ForeignKey(Client, verbose_name=_("for_client"), on_delete=models.CASCADE, blank=True, null=True)
    designation = models.CharField(_("Designation"), max_length=20)
    location = models.CharField(_("Job Location"), max_length=120, blank=True, null=True)
    job_type = models.CharField(_("Type"), max_length=50, choices=TYPE_CHOICES, blank=True, null=True)
    required_skills = TaggableManager(verbose_name="Required Skills", blank=True)
    description = HTMLField(_("Job description"), blank=True, null=True)
    min_salary = models.PositiveIntegerField(_("Minimum Salary"), blank=True, null=True)
    max_salary = models.PositiveIntegerField(_("Maximum Salary"), blank=True, null=True)
    requirements = models.IntegerField(_("Available Positions"), blank=True, null=True)
    min_experience = models.IntegerField(_("Minimum Experience"), blank=True, null=True)

    def __str__(self):
        return f'{self.designation} in {self.client.name}'

    def save(self, *args, **kwargs):
        if self.designation:
            if not self.client:
                print('Yes!!!!!!!!!!!!!!')
                self.client = self.agreement.client
            else:
                print('no............')
            super(JobDetail, self).save(*args, **kwargs)