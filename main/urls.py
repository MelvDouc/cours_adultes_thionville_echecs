from django.urls import path
from . import views

urlpatterns = [
    path("cours/categories/<str:slug>", views.category, name="category"),
    path("cours/<str:slug>", views.lesson, name="lesson"),
    path("cours/", views.lessons, name="lessons"),
    path("liens-utiles/", views.usefulLinks, name="useful-links"),
    path("contact/", views.contact, name="contact"),
    path("", views.home, name="home"),
    path("404/", views.notFound, name="not-found")
]
