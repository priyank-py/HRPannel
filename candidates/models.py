from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse
from stdimage import StdImageField, JPEGField
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from hr_profile.models import HRProfile
from tinymce.models import HTMLField
from taggit.managers import TaggableManager
from clients.models import Client, JobDetail


YEAR_CHOICES = [(i, i) for i in range(2000, datetime.date.today().year+3)] 

def upload_photo_to(instance, filename):
    return f'{instance.id}-{instance.name}/{filename}'

class Candidate(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    dob = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False)
    email = models.EmailField(_("Email"), max_length=254)
    phone_number = models.CharField(_("Phone No."), max_length=50)
    alternate_number = models.CharField(_("Alternate No."), max_length=50, blank=True, null=True)
    location = models.CharField(_("Location"), max_length=50)
    gender = models.CharField(_("Gender"), choices=(('male', 'Male'), ('female', 'Female')), max_length=50)
    designation = models.CharField(_("Designation"), max_length=50, blank=True, null=True)
    current_salary = models.FloatField(_("Current CTC (in LPA)"), blank=True, null=True)
    expected_salary = models.FloatField(_("Expected CTC (in LPA)"), blank=True, null=True)
    resume = models.FileField(_("Candidate Resume"), upload_to='Resumes/%d-%b', max_length=100, blank=True, null=True)
    photo = StdImageField(upload_to=upload_photo_to, blank=True, null=True, variations={
        'large': (640, 640),
        'medium': (300, 300),
        'thumbnail': (25, 25, True)
    }, delete_orphans=True)

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

    @property
    def total_experience(self):
        self.total = self.end - self.start
        self.total_years = self.total.days
        return self.total_years
    

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
    last_used = models.IntegerField(_("Last Used"), choices=YEAR_CHOICES, blank=True, null=True)

    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Skill_detail", kwargs={"pk": self.pk})


class Project(models.Model):
    candidate = models.ForeignKey(Candidate, verbose_name=_("Candidates"), on_delete=models.CASCADE)
    title = models.CharField(_("Project Title"), max_length=50, blank=True, null=True)
    technologies = TaggableManager(blank=True, verbose_name="Technologies Used")
    description = HTMLField(_("Description"), blank=True, null=True)
    role = models.CharField(_("Your Role"), max_length=50, blank=True, null=True)


class HRRemark(models.Model):

    STATUSES = (
        ('waiting', 'Waiting-List'),
        ('shortlisted', 'Short-Listed'),
        ('rejected', 'Rejected'),
        ('not_interested', 'Not-Interested')
    )

    candidate = models.ForeignKey(Candidate, blank=True, null=True, verbose_name=_("Candidates"), related_name="remarks", on_delete=models.CASCADE)
    hr = models.ForeignKey(HRProfile, verbose_name=_("HR"), on_delete=models.DO_NOTHING, blank=True, null=True)
    remark = models.CharField(_("Remarks"), max_length=150, blank=True, null=True)
    status = models.CharField(_("Status"), max_length=50, blank=True, null=True, choices=STATUSES)
    considered_for = models.ForeignKey(JobDetail, verbose_name=_("Considered for"), on_delete=models.DO_NOTHING, blank=True, null=True)
    reviewed_on = models.DateField(_("Reviewed on"), auto_now=False, auto_now_add=False)
    
