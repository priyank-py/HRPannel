from django.contrib import admin
from .models import Client, ContactPerson, Agreement, JobDetail
from taggit.admin import Tag
import nested_admin
from admin_numeric_filter.admin import (
    NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, SliderNumericFilter
) 
# Register your models here.

class CustomSliterAmountFilter(SliderNumericFilter):
    # MAX_DECIMALS = 1
    STEP = 500



class CustomSliderNumericFilter(SliderNumericFilter):
    MAX_DECIMALS = 7
    STEP = 0.1


class ContactPersonInline(nested_admin.NestedStackedInline):
    model = ContactPerson
    extra = 1


class JobDetailInline(nested_admin.NestedStackedInline):
    model = JobDetail
    fields = ['designation', 'location', 'job_type', 'required_skills', 'min_salary', 'max_salary', 'min_experience', 'requirements','description']
    
    extra = 1


class AgreementInline(nested_admin.NestedStackedInline):
    model = Agreement
    extra = 1
    
    inlines = (JobDetailInline,)

@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    ordering = ['end_date']
    list_display = ['title', 'agreement_status', 'start_date', 'end_date', 'commission']
    search_fields = ['title',]

@admin.register(JobDetail)
class JobDetailAdmin(NumericFilterModelAdmin):
    list_display = ['id', 'agreement', 'client', 'designation', 'min_salary', 'max_salary', 'min_experience',]
    list_display_links = ['id', 'agreement']
    exclude = ('client',)
    list_filter = ['client', 'client__company_type','designation', ('min_salary', RangeNumericFilter), ('max_salary', RangeNumericFilter), ('min_experience', CustomSliderNumericFilter)]
    search_fields = ['id', 'client', 'designation',]
    autocomplete_fields = ['agreement',]


@admin.register(Client)
class ClientAdmin(nested_admin.NestedModelAdmin, NumericFilterModelAdmin):
    list_display = ['name', 'company_type']
    list_filter = ['company_type', ('client_agreement__job_agreement__min_experience', CustomSliderNumericFilter)]
    exclude = ('client_agreement__job_agreement__client',)
    search_fields = ['name', 'address', 'client_cp__name', 'client_cp__contact_no', 'client_cp__alternate_no']
    inlines = (ContactPersonInline, AgreementInline)


# admin.site.register(Client)
admin.site.unregister(Tag)
# admin.site.register(JobDetail)