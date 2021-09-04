from django.shortcuts import render, HttpResponse


def home_page(request):
    return HttpResponse("Stylus Photography: Home")


def contact_page(request):
    return HttpResponse("Stylus Photography: Contact")


def about_page(request):
    return HttpResponse("Stylus Photography: About")


def gallery_page(request):
    return HttpResponse("Stylus Photography: Gallery")