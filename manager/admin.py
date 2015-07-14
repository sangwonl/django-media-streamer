from django.contrib import admin

from models import Preference
from models import Library


class PreferenceAdmin(admin.ModelAdmin):
    pass


class LibraryAdmin(admin.ModelAdmin):
    pass


admin.site.register(Preference, PreferenceAdmin)
admin.site.register(Library, LibraryAdmin)