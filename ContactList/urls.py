from django.conf.urls import patterns, include, url


urlpatterns = patterns('ContactList.views',
    url(r'^$', 'home', name='home'),


    # Used for Agenda
    url(r'^users/(?P<username>[-\w]+)/$', 'contact_list_user', name='app_contact_list_user'),
    url(r'^$', 'contact_lists', name='app_contact_lists'),
    url(r'^create/$', 'contact_list_create', name='app_contact_list_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'contact_list_edit', name='app_contact_list_edit'),

    # Used for Contacts
    url(r'^contactlist/(?P<contactListId>[-\w]+)/contacts/$', 'contacts', name='app_contacts'),
    url(r'^contactList/(?P<contactListId>[-\w]+)/contacts/create$', 'contact_create', name='app_contact_create'),
    url(r'^contacts/edit/(?P<pk>\d+)/$', 'contact_edit', name='app_contact_edit'),

    # Used for locations
    url(r'^contact/(?P<contactId>[-\w]+)/locations/$', 'locations', name='app_locations'),
    url(r'^contact/(?P<contactId>[-\w]+)/locations/create$', 'location_create', name='app_location_create'),
    url(r'^locations/edit/(?P<pk>\d+)/$', 'location_edit', name='app_location_edit'),

    # Used for social_networks
    url(r'^contact/(?P<contactId>[-\w]+)/socials/$', 'social_networks', name='app_social_networks'),
    url(r'^contact/(?P<contactId>[-\w]+)/socials/create$', 'social_network_create', name='app_social_network_create'),
    url(r'^socials/edit/(?P<pk>\d+)/$', 'social_network_edit', name='app_social_network_edit'),


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
)

