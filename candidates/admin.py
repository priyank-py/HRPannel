from django.contrib import admin
from .models import Candidate, Education, Experience, Certificate, Skill, HRRemark
import csv
from django.http import HttpResponse


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
    actions = ['export_to_csv',]

    def export_to_csv(self, request,queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response