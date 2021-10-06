from django.contrib import admin

from .models import PageInfo, HomePage, AboutPage

admin.site.register(PageInfo)
admin.site.register(HomePage)
admin.site.register(AboutPage)
