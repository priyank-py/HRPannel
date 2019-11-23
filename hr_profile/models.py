from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from PIL import Image


# Create your models here.
class HRProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE, blank=True, null=True)
    dob = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False)
    gender = models.CharField(_("Gender"), choices=(('male', 'Male'), ('female', 'Female')),max_length=10)
    hire_date = models.DateField(_("Hired on"), auto_now=False, auto_now_add=False)
    photo = models.ImageField(_("Photo"), upload_to='HR_Photos/%b-%Y', blank=True, null=True)
        

    class Meta:
        verbose_name = _("HRProfile")
        verbose_name_plural = _("HRProfiles")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("HRProfile_detail", kwargs={"pk": self.pk})
    
    def save(self, *args, **kwargs):
        super(HRProfile, self).save(*args, **kwargs)
        if self.id:
            previous = HRProfile.objects.get(id=self.id)
            if self.photo and self.photo != previous.photo:
                image = Image.open(self.photo.path)
                image = image.resize((96, 96), Image.ANTIALIAS)
                image.save(self.photo.path)
