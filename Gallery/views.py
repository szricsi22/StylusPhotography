from django.views.generic import TemplateView, DetailView

from utilities.data_gen import create_photo_list


class GalleryView(TemplateView):
    template_name = "gallery.html"

    def get_context_data(self, **kwargs):
        context = super(GalleryView, self).get_context_data(**kwargs)
        context["photos"] = create_photo_list(18)
        return context


class PhotoDetailView(TemplateView):
    template_name = "photo_details.html"
