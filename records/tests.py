from django.test import TestCase
from django.utils import timezone
from .models import EducationLevel, TeacherDesignation, Teacher, Attendance, Student


class StudentTest(TestCase):
    def setUp(self):
        teacher = Teacher.objects.create(
            name='Stive', joining_date=timezone.now())
        level = EducationLevel.objects.create(level="BSC")
        designation = TeacherDesignation.objects.create(
            designation="Class Teacher")
        student = Student.objects.create(
            first_name='Isack',
            middle_name="J",
            last_name="Jakes",
            guardian=None,
            administration_number="ST123456"
        )
        attendance = Attendance.objects.create(
            time_in=timezone.now(),
            time_out=timezone.now(),
            # present=False,
            # student=student
        )

    def test_count(self):
        tc = Teacher.objects.all()
        self.assertEqual(tc.count(), 1)

    def test_teacher_exist(self):
        qs = Teacher.objects.filter(name='Stive')
        self.assertTrue(qs.exists())

    def test_teacher_level(self):
        subj = EducationLevel.objects.filter(level='BSC')
        self.assertTrue(subj.exists())

    def test_designition(self):
        des = TeacherDesignation.objects.filter(designation="Class Teacher")
        self.assertTrue(des.exists())

    def test_teacher_joining_date(self):
        qs = Teacher.objects.filter(joining_date__lte=timezone.now())
        self.assertTrue(qs.exists())

    def test_student(self):
        qs = Student.objects.filter(administration_number="ST123456")
        self.assertTrue(qs.exists())

    def test_attendance(self):
        # nb = 'AD558851'
        qs = Attendance.objects.count()
        self.assertEqual(qs, 1)
        # qs = Attendance.objects.filter(student_admision_number=nb)
        # self.assertTrue(qs.exists())
