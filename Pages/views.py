from django.views.generic import TemplateView

from .models import HomePage, AboutPage


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        model_data_list = HomePage.objects.all()

        if not model_data_list:
            return context

        context["data"] = model_data_list[0]
        context["photo"] = "https://source.unsplash.com/500x500/?nature,water"
        return context


class ContactView(TemplateView):
    template_name = "contact.html"


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)

        about_data_list = AboutPage.objects.all()
        if not about_data_list:
            return context

        context["data"] = about_data_list[0]

        return context

