from django.contrib import admin

from .models import Category, Photo

admin.site.register(Category)


class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "frontpage", "image"]
    list_editable = ["frontpage"]
    list_filter = ["category"]
    search_fields = ["title"]


admin.site.register(Photo, PhotoModelAdmin)
