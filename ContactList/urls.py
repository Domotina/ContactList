from django.conf.urls import patterns, include, url


urlpatterns = patterns('ContactList.views',
    url(r'^$', 'contact_lists', name='home'),

    url(r'^users/(?P<username>[-\w]+)/$', 'contact_list_user', name='app_contact_list_user'),
    url(r'^$', 'contact_lists', name='app_contact_lists'),
    url(r'^create/$', 'contact_list_create', name='app_contact_list_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'contact_list_edit', name='app_contact_list_edit'),

    #url(r'^agenda/(?P<agendaId>[-\w]+)/contacts/$', 'contact_list', name='contacts_contact_list'),
    #url(r'^agenda/(?P<agendaId>[-\w]+)/contacts/create$', 'contact_create', name='contacts_contact_create'),
)

