from django.shortcuts import render
from utilities.data_gen import create_photo_list


def home_page(request):
    return render(request, "home.html")


def contact_page(request):
    return render(request, "contact.html")


def about_page(request):
    return render(request, "about.html")


def gallery_page(request):
    return render(request, "gallery.html", {"photos": create_photo_list(10)})
