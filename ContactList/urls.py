from django.conf.urls import patterns, include, url


urlpatterns = patterns('ContactList.views',
    url(r'^$', 'home', name='home'),

    # Used for Agenda
    url(r'^users/(?P<username>[-\w]+)/$', 'contact_list_user', name='app_contact_list_user'),
    url(r'^$', 'contact_lists', name='app_contact_lists'),
    url(r'^create/$', 'contact_list_create', name='app_contact_list_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'contact_list_edit', name='app_contact_list_edit'),

    # Used for Contacts
    url(r'^contactlist/(?P<contact_list_id>[-\w]+)/contacts/$', 'contacts', name='app_contacts'),
    url(r'^contactlist/(?P<contact_list_id>[-\w]+)/contacts/create$', 'contact_create', name='app_contact_create'),
    url(r'^contacts/edit/(?P<pk>\d+)/$', 'contact_edit', name='app_contact_edit'),

    # Used for locations
    url(r'^contact/(?P<contact_id>[-\w]+)/locations/$', 'locations', name='app_locations'),
    url(r'^contact/(?P<contact_id>[-\w]+)/locations/create$', 'location_create', name='app_location_create'),
    url(r'^locations/edit/(?P<pk>\d+)/$', 'location_edit', name='app_location_edit'),

    # Used for social_networks
    url(r'^contact/(?P<contact_id>[-\w]+)/socials/$', 'social_networks', name='app_social_networks'),
    url(r'^contact/(?P<contact_id>[-\w]+)/socials/create$', 'social_network_create', name='app_social_network_create'),
    url(r'^socials/edit/(?P<pk>\d+)/$', 'social_network_edit', name='app_social_network_edit'),

    # Used for company ??? contact_list_id??
    url(r'^contactlist/(?P<contact_list_id>[-\w]+)/company/create$', 'company_create', name='app_company'),


    url(r'^search/$', 'search', name='app_search'),
)

