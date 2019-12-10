from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _ 
from taggit.managers import TaggableManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import get_object_or_404

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
        return reverse("Client_detail", kwargs={"pk": self.pk})


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
    
    

    class Meta:
        verbose_name = _("Agreement")
        verbose_name_plural = _("Agreements")



class JobDetail(models.Model):
    agreement = models.ForeignKey(Agreement, verbose_name=_("agreement"), related_name="job_agreement", on_delete=models.CASCADE, blank=True, null=True)
    client = models.ForeignKey(Client, verbose_name=_("for_client"), on_delete=models.CASCADE, blank=True, null=True)
    designation = models.CharField(_("Designation"), max_length=50)
    required_skills = TaggableManager(verbose_name="Required Skills")
    min_salary = models.PositiveIntegerField(_("Minimum Salary"), blank=True, null=True)
    max_salary = models.PositiveIntegerField(_("Maximum Salary"), blank=True, null=True)
    requirements = models.IntegerField(_("Total Requirements"), blank=True, null=True)
    min_experience = models.IntegerField(_("Minimum Experience"), blank=True, null=True)

    def __str__(self):
        return self.designation

    def save(self, *args, **kwargs):
        if not self.client:
            print('Yes!!!!!!!!!!!!!!')
            client = self.agreement.client
        else:
            print('no............')
        super(JobDetail, self).save(*args, **kwargs)