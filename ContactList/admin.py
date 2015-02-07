from django.contrib import admin
from models import TypeData,LocationData, SocialNetworkType
# Register your models here.

class socialNetworkTypeAdmin:
    fields = ['name', 'icon']
    list_display = ('name', )
    list_editable = ('name', )
    list_filter = ('name', )
    search_fields = ('name', )
    #readonly_fields = ('name', )

admin.site.register(TypeData)
admin.site.register(LocationData)
admin.site.register(SocialNetworkType)