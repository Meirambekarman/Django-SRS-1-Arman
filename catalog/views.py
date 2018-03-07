from django.shortcuts import render

# Create your views here.

from .models import Student, Teacher, Location


def index(request):
    num_teachers = Teacher.objects.count()
    num_students = Student.objects.all().count()
    num_locations = Location.objects.count()

    return render(
        request,
        'index.html',
        context={'num_students': num_students, 'num_teachers': num_teachers, 'num_locations': num_locations},
    )


from django.views import generic


class TeacherListView(generic.ListView):
    model = Teacher
    paginate_by = 2


class TeacherDetailView(generic.DetailView):
    model = Teacher


class StudentListView(generic.ListView):
    model = Student
    paginate_by = 2


class StudentDetailView(generic.DetailView):
    model = Student

class LocationListView(generic.ListView):
    model = Location
    paginate_by = 2


class LocationDetailView(generic.DetailView):
    model = Location