from django.urls import path

from .views import home_page, gallery_page, contact_page, about_page


urlpatterns = [
    path("", home_page),
    path("contact/", contact_page),
    path("about/", about_page),
    path("gallery/", gallery_page)
]
