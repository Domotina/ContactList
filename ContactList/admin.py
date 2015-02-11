from django.contrib import admin
from models import LocationType, LocationPlace, SocialNetworkType,ThemeContactList


class SocialNetworkTypeAdmin(admin.ModelAdmin):
    fields = ['name', 'icon']
    list_display = ('name', 'icon')
    #list_editable = ('name', )
    list_filter = ('name', 'icon')
    search_fields = ('name', 'icon')
    #readonly_fields = ('name', )

admin.site.register(LocationType)
admin.site.register(LocationPlace)
admin.site.register(SocialNetworkType, SocialNetworkTypeAdmin)
admin.site.register(ThemeContactList)