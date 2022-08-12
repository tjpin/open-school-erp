from django.contrib import admin

from .models import Teacher, Attendance, Class

admin.site.register(Class)
admin.site.register(Teacher)
admin.site.register(Attendance)

