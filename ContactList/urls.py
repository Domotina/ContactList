from django.conf.urls import patterns, include, url


urlpatterns = patterns('ContactList.views',
    url(r'^$', 'contact_lists', name='home'),

    url(r'^users/(?P<username>[-\w]+)/$', 'contact_list_user', name='app_contact_list_user'),
    url(r'^$', 'contact_lists', name='app_contact_lists'),
    url(r'^create/$', 'contact_list_create', name='app_contact_list_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'contact_list_edit', name='app_contact_list_edit'),
    url(r'^viewContacts/(?P<pk>\d+)/$', 'app_contact_list_contact', name='app_contact_list_contact'),
    url(r'^createNewContact/(?P<pk>\d+)/$', 'app_create_contact', name='app_create_contact'),
    url(r'^createContact/(?P<pk>\d+)/$', 'app_contact_list_create_contact', name='app_contact_list_create_contact'),
    url(r'^createCompany/$', 'app_create_company', name='app_create_company'),
    url(r'^create_NewCompany/create_contact.html$', 'CompanyView', name='CompanyView'),
    url(r'^create_NewContact/listContact.html$', 'app_contact_list_create_contact', name='app_contact_list_create_contact'),
    url(r'^search/$', 'SearchContact', name='SearchContact'),
    url(r'^search/$', 'search', name='search'),
    url(r'^createLocation/$', 'create_location', name='create_location'),
    url(r'^createLocationData/$', 'create_location_data', name='create_location_data'),

    #url(r'^agenda/(?P<agendaId>[-\w]+)/contacts/$', 'contact_list', name='contacts_contact_list'),
    #url(r'^agenda/(?P<agendaId>[-\w]+)/contacts/create$', 'contact_create', name='contacts_contact_create'),
)

