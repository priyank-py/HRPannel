from django.contrib import admin
from .models import Candidate, Education, Experience, Certificate, Skill, HRRemark
# Register your models here.


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 1


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1


class EducationInline(admin.TabularInline):
    model = Education
    extra = 1


class HRRemarkInline(admin.TabularInline):
    model = HRRemark
    extra = 1



@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    inlines = (EducationInline, ExperienceInline, CertificateInline, SkillInline, HRRemarkInline)
    
