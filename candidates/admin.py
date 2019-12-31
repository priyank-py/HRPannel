from django.contrib import admin
from .models import Candidate, Education, Experience, Certificate, Skill, HRRemark, Project
import csv
from datetime import timedelta
from django.http import HttpResponse
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, \
    SliderNumericFilter


class CustomSliderNumericFilter(SliderNumericFilter):
    MAX_DECIMALS = 2
    STEP = 1


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

class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1

class HRRemarkInline(admin.TabularInline):
    model = HRRemark
    extra = 1


@admin.register(Candidate)
class CandidateAdmin(NumericFilterModelAdmin):

    def total_experience(self, instance):
        total = 0
        for exp in instance.experiences.all():
            total += exp.total_experience
        return f'{int(total//365.2425)} years, {int((total%365.2425)//30.436875)} months'


    inlines = (EducationInline, ExperienceInline, CertificateInline, SkillInline, ProjectInline, HRRemarkInline)
    list_display = ['id', 'name', 'phone_number', 'total_experience']
    list_filter = ['educations__qualification', ('educations__marks', CustomSliderNumericFilter), ('current_salary',  CustomSliderNumericFilter), ('expected_salary', CustomSliderNumericFilter)]
    actions = ['export_to_csv',]

    def export_to_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response