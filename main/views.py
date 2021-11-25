from django.shortcuts import redirect, render
from .forms import MessageForm
from .models import Category, Lesson
from .utils import calculate_age, get_std_rating


def home(req):
    age = calculate_age()
    std_rating = get_std_rating()
    return render(req, "main/home.html", {
        "title": "Accueil",
        "age": age,
        "std_rating": std_rating
    })


def notFound(req):
    return render(req, "main/404.html")


def category(req, slug):
    try:
        cat = Category.objects.get(slug=slug)
        lessons = Lesson.objects.filter(category=cat)
        return render(req, "main/category.html", {
            "title": cat.name,
            "category": cat,
            "lessons": lessons
        })
    except:
        return redirect("/404")


def lessons(req):
    categories = Category.objects.all()
    return render(req, "main/lessons.html", {
        "title": "Cours",
        "categories": categories
    })


def lesson(req, slug):
    try:
        lesson = Lesson.objects.get(slug=slug)
        return render(req, f"main/lessons/{lesson.slug}.html", {
            "title": lesson.name
        })
    except:
        return redirect("/404")


def usefulLinks(req):
    links = [
        {
            "url": "http://club.quomodo.com/thionville-echecs",
            "text": "Site du club de Thionville"
        },
        {
            "url": "https://www.youtube.com/channel/UC9BJqAqRlOJBAA0O4WYSmnw/videos",
            "text": "Chaine Youtube des cours"
        },
        {
            "url": "https://lichess.org/team/thionville-echecs",
            "text": "Club de Thionville sur Lichess"
        },
        {
            "url": "https://www.facebook.com/thionville.echecs/",
            "text": "Page Facebook du club"
        },
        {
            "url": "https://www.instagram.com/thionvilleechecs/",
            "text": "Compte Instagram du club"
        }
    ]
    return render(req, "main/useful-links.html", {
        "title": "Liens utiles",
        "links": links
    })


def contact(req):
    if req.method == "GET":
        form = MessageForm(label_suffix="")
        return render(req, "main/contact.html", {
            "title": "Me contacter",
            "form": form
        })
    form = MessageForm(req.POST)
    if not form.is_valid():
        return redirect("/contact")
    form.save()
    return redirect("/")

