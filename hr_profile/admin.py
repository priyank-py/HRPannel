from django.contrib import admin
from .models import HRProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class HRProfileInline(admin.StackedInline):
    model = HRProfile
    extra = 1
    min_num = 1
    max_num = 1

class HRProfileUserAdmin(UserAdmin):
    inlines = (HRProfileInline,)
    list_select_related = ('profile',)


    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(HRProfileUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, HRProfileUserAdmin)
