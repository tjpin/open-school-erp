from django.db import models

from records.models import Student, Teacher
from students.models import Parent


class BookCategory(models.Model):
    category = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = 'Book Category'
        verbose_name_plural = 'Book Categories'

    def __str__(self) -> str:
        return self.category


class BookCondition(models.TextChoices):
    NEW = ('NW', "New")
    AS_NEW = ('AN', "As New")
    GOOD = ('GD', "Good")
    OLD = ('OD', "Old")


class Book(models.Model):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    section = models.CharField(max_length=20, null=True, blank=True)
    publisher = models.CharField(max_length=50)
    shelf_number = models.CharField(max_length=20)
    date_published = models.DateTimeField(null=True, blank=True)
    date_borrowered = models.DateTimeField(null=True, blank=True)
    date_returned = models.DateTimeField(null=True, blank=True)
    is_returned = models.BooleanField(default=False, null=True, blank=True)
    book_number = models.CharField(max_length=10, null=True, blank=True)
    issued_by = models.ForeignKey(
        Teacher, null=True, blank=True, on_delete=models.SET_NULL)
    borrower = models.ForeignKey(
        Student, null=True, blank=True, on_delete=models.SET_NULL)
    isbn = models.CharField(max_length=20, null=True, blank=True)
    date_puchased = models.DateTimeField(null=True, blank=True)
    edition = models.CharField(max_length=30, null=True, blank=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    condition = models.CharField(
        choices=BookCondition.choices, max_length=50, null=True, blank=True)
    category = models.ForeignKey(
        BookCategory, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self) -> str:
        return self.name

class Library(models.Model):
    # books_total = Book.objects.count()
    name = models.CharField(max_length=50, null=True, blank=True)
    books = models.ManyToManyField(Book)
    incharge = models.ForeignKey(
        Teacher, null=True, blank=True, on_delete=models.SET_NULL)
    opening_time = models.DateTimeField(null=True, blank=True)
    closing_time = models.DateTimeField(null=True, blank=True)
    lost_books = models.ManyToManyField(
        Book, related_name='lost_books', null=True, blank=True)
    replaced_books = models.ManyToManyField(
        Book, related_name='replaced_books', null=True, blank=True)

    class Meta:
        verbose_name = 'Library'
        verbose_name_plural = 'Libraries'

    def __str__(self) -> str:
        return self.name
