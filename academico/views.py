from django.shortcuts import get_object_or_404, render, redirect
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
        return render(
            request, "manage_courses.html", {"courses": courses, "error": error}
        )

    return redirect(reverse("academico:home"))


def delete_course(request, id):
    course = get_object_or_404(Course, pk=id)
    course.delete()

    return redirect(reverse("academico:home"))


def edit_course(request, id):
    course = get_object_or_404(Course, pk=id)
    return render(request, "edit_course.html", {"course": course})


def update_course(request, id):
    try:
        course = get_object_or_404(Course, pk=id)
        name = request.POST["course_name"].strip().lower()
        credits = request.POST["credits"]

        if name == "":
            raise Exception("The course must have a name")

        if int(credits) < 0:
            raise Exception("The credits mus be greather than 0")

        course.name = name
        course.credits = credits
        course.save()
    except Exception as error:
        return render(request, "edit_course.html", {"course": course, "error": error})

    return redirect(reverse("academico:home"))
