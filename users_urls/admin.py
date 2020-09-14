from django.contrib import admin

from .models import Urls


class UrlsAdmin(admin.ModelAdmin):
	search_fields = ('user',)


admin.site.register(Urls, UrlsAdmin)
