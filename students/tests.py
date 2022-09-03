from django.test import TestCase
from .models import Student, Parent, Subject
from classes.models import Class


class StudentTest(TestCase):
    def setUp(self):
        class_ = Class.objects.create(class_name="Form 3 South")
        subject_ = Subject.objects.create(subject="Maths")

        self.student = Student.objects.create(
            first_name='Peter',
            middle_name='Walker',
            last_name='Jones',
            class_level=class_,
        )

    def test_count(self):
        st = Student.objects.all()
        self.assertEqual(st.count(), 1)

    def test_student_exist(self):
        qs = Student.objects.filter(first_name='Peter')
        self.assertTrue(qs.exists())

    def test_subject(self):
        subj = Subject.objects.filter(subject='Maths')
        self.assertTrue(subj.exists())
