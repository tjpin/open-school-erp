from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *

# *************** Admin Models ***************************
# ********************************************************


class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'administration_number',
                    'level', 'class_level', 'guardian']
    list_filter = ['level', 'class_level']
    list_display_links = ['first_name', 'last_name', 'guardian']
    search_fields = ['first_name', 'administration_number']

    class Meta:
        model = Student


class ParentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name',
                    'relationship', 'phone_number', 'related_student_number']
    list_filter = ['relationship', ]
    list_display_links = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']

    class Meta:
        model = Parent


# *************** Staffs Models **************************
# ********************************************************
admin.site.unregister(Group)

admin.site.register(Parent, ParentAdmin)
admin.site.register(Subject)
admin.site.register(Student, StudentAdmin)
