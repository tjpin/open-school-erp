from django.db import models


class Class(models.Model):

    class_name = models.CharField(max_length=20)
    objects = models.Manager()
    # total_students = models.IntegerField(help_text='Number of students', default=len(list(total)))

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name = "Class"
        verbose_name_plural = "Classes"
