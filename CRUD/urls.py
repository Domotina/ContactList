from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'CRUD.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    #url(r'^erase/(?P<id_contact>\d+)$', 'ContactList.views.erase_contact', name='erase_contact'),
    #url(r'^edit/(?P<id_contact>\d+)$', 'ContactList.views.edit_contact', name='edit_contact'),
    #url(r'^create/$', 'ContactList.views.create_contact', name='create_contact'),

    url(r'^$', 'ContactList.views.index', name='index'),
    url(r'^company/', 'ContactList.views.CompanyView', name='company'),
    url(r'^list/', 'ContactList.views.ListView', name='list'),
    url(r'^contact/', 'ContactList.views.ContactView', name='contact'),
    url(r'^location/', 'ContactList.views.LocationView', name='location'),
    url(r'^address/', 'ContactList.views.AddressView', name='address'),
    url(r'^email/', 'ContactList.views.EmailView', name='email'),
    url(r'^phone/', 'ContactList.views.PhoneView', name='phone'),
    url(r'^create/', 'ContactList.views.create', name='create'),
)
