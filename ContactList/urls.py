from django.conf.urls import patterns, include, url


urlpatterns = patterns('ContactList.views',
    url(r'^user/(?P<username>[-\w]+)/$', 'agenda_user', name='contacts_agenda_user'),
    url(r'^$', 'agenda_list', name='contacts_agenda_list'),
    url(r'^create/$', 'agenda_create', name='contacts_agenda_create'),
    url(r'^edit/(?P<pk>\d+)/$', 'agenda_edit', name='contacts_agenda_edit'),

    url(r'^agenda/(?P<agendaId>[-\w]+)/contacts/$', 'contact_list', name='contacts_contact_list'),
    url(r'^agenda/(?P<agendaId>[-\w]+)/contacts/create$', 'contact_create', name='contacts_contact_create'),
)

