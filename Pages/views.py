from django.shortcuts import render


def home_page(request):
    context = {
        "page_title": "Stylus Photography",
        "subtitle": "Ha már unod az egyforma képeket..."
    }
    return render(request, "home.html", context)


def contact_page(request):
    return render(request, "contact.html")


def about_page(request):
    return render(request, "about.html")


def gallery_page(request):
    return render(request, "gallery.html")
