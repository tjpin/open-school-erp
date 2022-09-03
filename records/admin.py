from django.contrib import admin

from .models import Teacher, Attendance, TeacherDesignation, EducationLevel


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'contract',
                    'on_duty', 'subjects', 'joining_date']

    class Meta:
        model = Teacher


class AttendanceAdmin(admin.ModelAdmin):
    list_display = ['student', 'time_in', 'time_out',
                    'weekend', 'student_admision_number']
    list_filter = ['weekend']
    list_display_links = ['student', 'time_in', 'time_out']
    search_fields = ['student', 'weekend']

    class Meta:
        model = Attendance


admin.site.register(TeacherDesignation)
admin.site.register(EducationLevel)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Attendance, AttendanceAdmin)
