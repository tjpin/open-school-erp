from django.db.models import Q
from django.views.generic import ListView

from . models import Student, Subject


class HomeView(ListView):
    model = Student
    template_name = 'students/index.html'
    context_object_name = 'students'
    queryset = Student.objects.all()

    def get_queryset(self):
        # a = Q()
        return Student.objects.all()
