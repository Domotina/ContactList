from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AgendaForm, ContactoForm
from .models import Agenda, Contacto

def agenda_list(request):
    agendas = Agenda.public.all()
    context = {'agendas': agendas}
    return render(request, 'agenda_list.html', context)

def contact_list(request, agendaId):
    agenda = get_object_or_404(Agenda, id = agendaId)
    contactos = agenda.contactos.all()
    context = {'contactos': contactos, 'agendaId': agendaId}
    return render(request, 'contact_list.html', context)

def agenda_user(request, username):
    user = get_object_or_404(User, username = username)
    if request.user == user:
        agendas = user.agendas.all()
    else:
        agendas = Agenda.public.filter(propietario__username = username)
    context = {'agendas': agendas, 'propietario': user}
    return render(request, 'agenda_user.html', context)

@login_required
def agenda_create(request):
    if request.method == 'POST':
        form = AgendaForm(data = request.POST)
        if form.is_valid():
            form.save(propietario = request.user)
            return redirect('contacts_agenda_user', username = request.user.username)
    else:
        form = AgendaForm()
    return render(request, 'form.html', {'form': form, 'create': True})

@login_required
def contact_create(request, agendaId):
    if request.method == 'POST':
        form = ContactoForm(data = request.POST)
        if form.is_valid():
            form.save()
            print(agendaId)
            return redirect('contacts_contact_list', agendaId = agendaId)
    else:
        form = ContactoForm()
    return render(request, 'form.html', {'form': form, 'create': True})

@login_required
def agenda_edit(request, pk):
    agenda = get_object_or_404(Agenda, pk = pk)
    if agenda.propietario != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = AgendaForm(instance = agenda, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts_agenda_user', username = request.user.username)
    else:
        form = AgendaForm(instance = agenda)
    return render(request, 'form.html', {'form': form, 'create': False, 'agenda': agenda})