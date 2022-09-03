from django.utils import timezone
from django.db import models
from datetime import datetime as dt

from students.models import Student, Subject
from classes.models import Class


class CustomDateTimeField(models.DateTimeField):

    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0, second=0)
            return val.isoformat()
        return ''


class TeacherDesignation(models.Model):
    designation = models.CharField(max_length=30)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name = "Teacher Designation"
        verbose_name_plural = "Teacher Designations"


class EducationLevel(models.Model):
    level = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.level

    class Meta:
        verbose_name = "Education Levels"
        verbose_name_plural = "Education Level"


class Teacher(models.Model):
    job_types = [("CT", "Contract"), ("PT", "Part Time"), ("PNT", "Permanent")]

    joining_date = models.DateField(default=timezone.now())
    name = models.CharField(max_length=30)
    contract = models.CharField(
        choices=job_types, max_length=20, null=True, blank=True)
    id_number = models.IntegerField(default=0, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    on_duty = models.BooleanField(default=False, null=True, blank=True)
    phone_number = models.IntegerField(default=0, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True, max_length=50)
    on_probation = models.BooleanField(default=False, null=True, blank=True)
    certificate_number = models.CharField(max_length=30, null=True, blank=True)
    subjects = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(
        EducationLevel, on_delete=models.SET_NULL, null=True, blank=True)
    certificate = models.FileField(
        upload_to='certificates', null=True, blank=True)
    designation = models.ForeignKey(
        TeacherDesignation, on_delete=models.SET_NULL, null=True)
    class_in_charge = models.ForeignKey(
        Class, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"


class Attendance(models.Model):
    weekends = [("WD", "Weekday"), ('SAT', "Saturday"),
                ('SUN', "Sunday"), ("HD", "Holiday")]
    time_in = CustomDateTimeField()
    time_out = CustomDateTimeField()
    present = models.BooleanField(default=True, null=True, blank=True)
    weekend = models.CharField(
        choices=weekends, max_length=100, null=True, blank=True)
    student = models.ForeignKey(
        Student, on_delete=models.SET_NULL, null=True, blank=True)
    reason_for_absence = models.TextField(
        max_length=500, null=True, blank=True)
    absent_with_permission = models.BooleanField(
        default=True, null=True, blank=True)
    permission_by_teacher = models.ForeignKey(
        Teacher, on_delete=models.SET_NULL, null=True, blank=True, default="N/A")

    def __str__(self):
        return self.student.first_name

    def set_time_in(self):
        return self.time_in

    def student_admision_number(self):
        return self.student.student_admin_number

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendance"
