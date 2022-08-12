from django.db import models
from students.models import Student, Subject


class Class(models.Model):
    total = Student.objects.all()

    class_name = models.CharField(max_length=20)
    total_students = models.IntegerField(help_text='Number of students', default=len(list(total)))

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"


class TeacherDesignation(models.Model):
    designation = models.CharField(max_length=30)

    def __str__(self):
        return self.designation

    class Meta:
        verbose_name = "TeacherDesignation"
        verbose_name_plural = "TeacherDesignation"


class EducationLevel(models.Model):
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.level

    class Meta:
        verbose_name = "EducationLevel"
        verbose_name_plural = "EducationLevel"


class Teacher(models.Model):
    job_types = [("CT", "Contract"), ("PT", "Part Time"), ("PNT", "Permanent")]

    joining_date = models.DateField()
    name = models.CharField(max_length=30)
    id_number = models.IntegerField(default=0)
    phone_number = models.IntegerField(default=0)
    on_probation = models.BooleanField(default=False)
    certificate_number = models.CharField(max_length=30)
    contract = models.CharField(choices=job_types, max_length=20)
    address = models.CharField(max_length=100, null=True, blank=True)
    on_duty = models.BooleanField(default=False, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True, max_length=50)
    subjects = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(EducationLevel, on_delete=models.SET_NULL, null=True)
    certificate = models.FileField(upload_to='certificates', null=True, blank=True)
    designation = models.ForeignKey(TeacherDesignation, on_delete=models.SET_NULL, null=True)
    class_in_charge = models.ForeignKey(Class, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"


class Attendance(models.Model):
    weekends = [("WD", "Weekday"), ('SAT', "Saturday"), ('SUN', "Sunday"), ("HD", "Holiday")]

    time_in = models.DateTimeField()
    time_out = models.DateTimeField()
    present = models.BooleanField(default=True)
    weekend = models.CharField(choices=weekends, max_length=100)
    student = models.ForeignKey(Student, on_delete=models.SET_NULL, null=True)
    reason_for_absence = models.TextField(max_length=500, null=True, blank=True)
    absent_with_permission = models.BooleanField(default=True, null=True, blank=True)
    permission_by_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True, default="N/A")

    def __str__(self):
        return self.student.first_name

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendance"

