from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_Page, name="home"),
    path('courseview/', views.course_view, name="courseView")
]