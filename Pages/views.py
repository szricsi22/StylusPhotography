from django.views.generic import TemplateView, FormView

from .models import HomePage, AboutPage
from Gallery.models import Photo
from .forms import ContactForm
from django.core.mail import send_mail

import random


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        model_data_list = HomePage.objects.all()

        if not model_data_list:
            return context

        context["data"] = model_data_list[0]

        frontpage_photo_list = Photo.objects.filter(frontpage=True)
        if frontpage_photo_list:
            context["photo"] = random.choice(frontpage_photo_list)

        return context


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/contact/sent/"

    def form_valid(self, form):
        name = form.data["name"]
        email = form.data["email"]
        message = form.data["message"]

        email_message = f"Name: {name}\n\n"
        email_message += message

        send_mail('Contact', email_message, email, ['szabo.ricsi22@gmail.com'], fail_silently=False)

        return super(ContactView, self).form_valid(form)


class ContactSentView(TemplateView):
    template_name = "email_sent.html"


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)

        about_data_list = AboutPage.objects.all()
        if not about_data_list:
            return context

        context["data"] = about_data_list[0]

        return context
