from django.shortcuts import render

# Create your views here.
def home_Page(request):
    return render(request, "courses/home.html", {})


def course_view(request):
    return render(request, "courses/courseView.html", {})