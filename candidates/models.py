from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from hr_profile.models import HRProfile

YEAR_CHOICES = [(i, i) for i in range(2000, datetime.date.today().year + 1)]

class Candidate(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    dob = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False)
    email = models.EmailField(_("Email"), max_length=254)
    phone_number = models.CharField(_("Phone No."), max_length=50)
    alternate_number = models.CharField(_("Alternate No."), max_length=50, blank=True, null=True)
    location = models.CharField(_("Location"), max_length=50)
    gender = models.CharField(_("Gender"), choices=(('male', 'Male'), ('female', 'Female')), max_length=50)
    

    class Meta:
        verbose_name = _("Candidate")
        verbose_name_plural = _("Candidates")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Candidate_detail", kwargs={"pk": self.pk})


class Education(models.Model):
    LEVEL_CHOICES = (
        ('doctorate', 'Doctorate'),
        ('masters', 'masters'),
        ('bachelors', 'Bachelors'),
        ('high_school', 'High School/PUC'),
    )
    
    candidate = models.ForeignKey(Candidate, verbose_name=_("Candidate"), related_name="educations", on_delete=models.CASCADE)
    qualification = models.CharField(_("Education level"), choices=LEVEL_CHOICES, max_length=50, blank=True, null=True)
    degree = models.CharField(_("Degree Qualified"), max_length=80)
    start = models.IntegerField(_("From"), choices=YEAR_CHOICES)
    end = models.IntegerField(_("till"), choices=YEAR_CHOICES)
    college_name = models.CharField(_("College Name"), max_length=80)
    marks = models.FloatField(_("Marks Obtained"), validators=[MinValueValidator(39.99), MaxValueValidator(100)])


    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Educations")
    
    def __str__(self):
        return self.degree
    

    def get_absolute_url(self):
        return reverse("Education_detail", kwargs={"pk": self.pk})


class Experience(models.Model):
    candidate = models.ForeignKey(Candidate, verbose_name=_("Candidate"), related_name='experiences', on_delete=models.CASCADE)
    company = models.CharField(_("Company Name"), max_length=50)
    job_profile = models.CharField(_("Job Profile"), max_length=50)
    current_company = models.BooleanField(_("Is this you current company?"), choices=((True, 'Yes'), (False, 'No')), blank=True, null=True)
    start = models.DateField(_("Started on"), auto_now=False, auto_now_add=False, blank=True, null=True)
    end = models.DateField(_("Worked Till"), auto_now=False, auto_now_add=False, blank=True, null=True)


    class Meta:
        verbose_name = _("Experience")
        verbose_name_plural = _("Experiences")

    def __str__(self):
        return self.company


    def get_absolute_url(self):
        return reverse("Experience_detail", kwargs={"pk": self.pk})


class Certificate(models.Model):
    candidate= models.ForeignKey(Candidate, verbose_name=_("Candidate"), related_name='certificates', on_delete=models.CASCADE)
    name = models.CharField(_("Certification Name"), max_length=50)
    organisation = models.CharField(_("Issuing Organisation"), max_length=50)
    issue = models.DateField(_("Issue Date"), auto_now=False, auto_now_add=False, blank=True, null=True)
    expire = models.DateField(_("Expiration Date"), auto_now=False, auto_now_add=False, blank=True, null=True)
    certificate_id = models.CharField(_("Credential ID"), max_length=50, blank=True, null=True)
    certificate_url = models.URLField(_("Credential URL"), max_length=200, blank=True, null=True)
    

    class Meta:
        verbose_name = _("Certificate")
        verbose_name_plural = _("Certificates")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Certificate_detail", kwargs={"pk": self.pk})

class Skill(models.Model):
    candidate = models.ForeignKey(Candidate, verbose_name=_("Candidates"), related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(_("Skill"), max_length=50)
    experience = models.IntegerField(_("Experience (in Years)"),  validators=[MinValueValidator(0), MaxValueValidator(100)], blank=True, null=True)
    last_used = models.IntegerField(_("till"), choices=YEAR_CHOICES, blank=True, null=True)

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Skill_detail", kwargs={"pk": self.pk})


class HRRemark(models.Model):
    candidate = models.ForeignKey(Candidate, verbose_name=_("Candidates"), related_name="remarks", on_delete=models.CASCADE)
    hr = models.ForeignKey(HRProfile, verbose_name=_("HR"), on_delete=models.CASCADE)
    remark = models.CharField(_("Remarks"), max_length=150)
    reviewed_on = models.DateField(_("Reviewed on"), auto_now=False, auto_now_add=False, default=timezone.now)
    

    class Meta:
        verbose_name = _("HRRemark")
        verbose_name_plural = _("HRRemarks")

    def __str__(self):
        return f'{self.hr.user.username} review {self.candidate.name}'

    def get_absolute_url(self):
        return reverse("HRRemark_detail", kwargs={"pk": self.pk})

