from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactListForm
from .models import ContactList

def contact_lists(request):
    contact_lists = ContactList.public.all()
    context = {'contact_lists': contact_lists}
    return render(request, 'contact_lists.html', context)

def contact_list_user(request, username):
    user = get_object_or_404(User, username = username)
    if request.user == user:
        contact_lists = user.contact_lists.all()
    else:
        contact_lists = ContactList.public.filter(owner_list__username = username)
    context = {'contact_lists': contact_lists, 'owner_list': user}
    return render(request, 'contact_list_user.html', context)

@login_required
def contact_list_create(request):
    if request.method == 'POST':
        form = ContactListForm(data = request.POST)
        if form.is_valid():
            form.save(owner_list = request.user)
            return redirect('app_contact_list_user', username = request.user.username)
    else:
        form = ContactListForm()
    return render(request, 'form.html', {'form': form, 'create': True})

@login_required
def contact_list_edit(request, pk):
    contact_list = get_object_or_404(ContactList, pk = pk)
    if contact_list.owner_list != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = ContactListForm(instance = contact_list, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_contact_list_user', username = request.user.username)
    else:
        form = ContactListForm(instance = contact_list)
    return render(request, 'form.html', {'form': form, 'create': False, 'contact_list': contact_list})

#def contact_list(request, agendaId):
#    agenda = get_object_or_404(Agenda, id = agendaId)
#    contactos = agenda.contactos.all()
#    context = {'contactos': contactos, 'agendaId': agendaId}
#    return render(request, 'contact_list.html', context)

#@login_required
#def contact_create(request, agendaId):
#    if request.method == 'POST':
#        form = ContactoForm(data = request.POST)
#        if form.is_valid():
#            form.save()
#            print(agendaId)
#            return redirect('contacts_contact_list', agendaId = agendaId)
#    else:
#        form = ContactoForm()
#    return render(request, 'form.html', {'form': form, 'create': True})