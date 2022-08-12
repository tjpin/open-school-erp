from django.db import models

import datetime as dt


class Subject(models.Model):
    subject = models.CharField(max_length=20, null=True, default="")
    objects = models.Manager()

    class Meta:
        ordering = ['subject']
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"

    def __str__(self):
        return self.subject


class Parent(models.Model):
    relationships = [("PR", "Parent"), ("GR", "Guardian"), ]
    occupations = [("EP", "Employed"), ("CL", "Casual"), ("UE", "Unemployed"), ]

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    phone_number = models.IntegerField()
    alternative_phone_number = models.IntegerField(null=True, blank=True)
    relationship = models.CharField(choices=relationships, default='Parent', max_length=20)
    id_number = models.IntegerField()
    occupation = models.CharField(choices=occupations, default='Employed', max_length=20)

    class Meta:
        ordering = ['first_name']
        verbose_name = "Parent"
        verbose_name_plural = "Parents"

    def __str__(self):
        return self.first_name


class Student(models.Model):
    levels = [('F1', 'Form One'), ('F2', 'Form Two'), ('F3', 'Form Three'), ('F4', 'Form Four')]

    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    picture = models.ImageField(upload_to="profiles", default="", null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    birth_certificate_number = models.CharField(max_length=15)
    calling_letter_number = models.CharField(max_length=20, null=True, blank=True)
    previous_level_certificate_number = models.CharField(max_length=20)
    entry_grade = models.CharField(max_length=20)
    guardian = models.ForeignKey(Parent, null=True, on_delete=models.SET_NULL)
    subjects = models.ManyToManyField(Subject)
    date_of_joining = models.DateTimeField()
    graduation_year = models.DateField()
    level = models.CharField(choices=levels, default="Form One", max_length=20)

    objects = models.Manager()

    class Meta:
        ordering = ['first_name']
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.first_name
