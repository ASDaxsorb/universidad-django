from traceback import TracebackException
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Course


def home(request):
    courses = Course.objects.all()
    return render(request, "manage_courses.html", {"courses": courses})


def add_course(request):

    try:
        course_name = request.POST["course_name"]
        credits = request.POST["credits"]

        if course_name.strip() == "":
            raise Exception("The course must contain a name")

        Course.objects.create(name=course_name, credits=credits)
    except Exception as error:
        courses = Course.objects.all()
        return redirect(reverse("academico:home", kwargs={"error": error}))

    return redirect(reverse("academico:home"))
