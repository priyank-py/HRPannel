from django.contrib import admin
from .models import Client, ContactPerson, Agreement, JobDetail
from taggit.admin import Tag
import nested_admin
from admin_numeric_filter.admin import NumericFilterModelAdmin, SingleNumericFilter, RangeNumericFilter, \
    SliderNumericFilter
# Register your models here.


class CustomSliderNumericFilter(SliderNumericFilter):
    MAX_DECIMALS = 2
    STEP = 1


class ContactPersonInline(nested_admin.NestedStackedInline):
    model = ContactPerson
    extra = 1


class JobDetailInline(nested_admin.NestedTabularInline):
    model = JobDetail
    
    extra = 1


class AgreementInline(nested_admin.NestedStackedInline):
    model = Agreement
    extra = 1
    
    inlines = (JobDetailInline,)


@admin.register(Client)
class ClientAdmin(nested_admin.NestedModelAdmin, NumericFilterModelAdmin):
    list_display = ['name', 'company_type']
    list_filter = ['company_type', ('client_agreement__job_agreement__min_experience', CustomSliderNumericFilter)]
    exclude = ('client_agreement__job_agreement__client',)
    inlines = (ContactPersonInline, AgreementInline)


# admin.site.register(Client)
admin.site.unregister(Tag)