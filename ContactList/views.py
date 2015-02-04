from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.template import RequestContext
from django.db.models import Q

from .forms import ContactListForm, ContactForm, CompanyForm, SearchForm, LocationDataForm, LocationForm
from .models import ContactList, Contact, Location, LocationData


def contact_lists(request):
    contact_lists = ContactList.public.all()
    context = {'contact_lists': contact_lists}
    return render(request, 'contact_lists.html', context)


def contact_list_user(request, username):
    user = get_object_or_404(User, username=username)
    if request.user == user:
        contact_lists = user.contact_lists.all()
    else:
        contact_lists = ContactList.public.filter(owner_list__username=username)
    context = {'contact_lists': contact_lists, 'owner_list': user}
    return render(request, 'contact_list_user.html', context)


@login_required
def contact_list_create(request):
    if request.method == 'POST':
        form = ContactListForm(data=request.POST)
        if form.is_valid():
            form.save(owner_list=request.user)
            return redirect('app_contact_list_user', username=request.user.username)
    else:
        form = ContactListForm()
    return render(request, 'form.html', {'form': form, 'create': True})


@login_required
def contact_list_edit(request, pk):
    contact_list = get_object_or_404(ContactList, pk=pk)
    if contact_list.owner_list != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = ContactListForm(instance=contact_list, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_contact_list_user', username=request.user.username)
    else:
        form = ContactListForm(instance=contact_list)
    return render(request, 'form.html', {'form': form, 'create': False, 'contact_list': contact_list})


def app_contact_list_contact(request, pk):
    try:
        # Ojo hay que validar bien
        contacts = Contact.objects.all()
    except Contact.DoesNotExist:
        contacts = None
    return render_to_response('listContact.html', {"contacts": contacts}, context_instance=RequestContext(request))


def app_create_contact(request, pk):
    form = ContactForm(request.POST or None)
    return render_to_response('create_contact.html', locals(), context_instance=RequestContext(request))


def app_contact_list_create_contact(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            save_it = form.save(commit=True)
            save_it.save()
            return redirect('../viewContacts/' + str(form.instance.contact_list.id))
    else:
        form = ContactForm()
    return render(request, 'create_contact.html', {'form': form, 'create': True})


def app_create_company(request):
    form = CompanyForm(request.POST or None)
    return render_to_response('create_company.html', locals(), context_instance=RequestContext(request))


def CompanyView(request):
    if request.method == 'POST':
        form = CompanyForm(data=request.POST)
        if form.is_valid():
            save_it = form.save(commit=True)
            save_it.save()
            return redirect('../createNewContact', username=request.user.username)
    else:
        form = CompanyForm()
    return render(request, 'create_contact.html', {'form': form, 'create': True})


def create_location(request):
    if request.method == 'POST':
        form = LocationForm(data=request.POST)
        if form.is_valid():
            save_it = form.save(commit=True)
            save_it.save()
            return render_to_response('create_location_data.html', locals(), context_instance=RequestContext(request))
    else:
        form = LocationForm()
    return render(request, 'create_location.html', {'form': form, 'create': True})

def create_location_data(request):
    if request.method == 'POST':
        form = LocationDataForm(data=request.POST)
        if form.is_valid():
            save_it = form.save(commit=True)
            save_it.save()
            return redirect('../viewContacts/' + str(form.instance.contact_list.id))
    else:
        form = LocationDataForm()
    return render(request, 'create_location_data.html', {'form': form, 'create': True})

def SearchContact(request):
    return render_to_response('search_contact.html', locals(), context_instance=RequestContext(request))


def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(name__icontains=query) |
            Q(last_name__icontains=query)
        )
        results = Contact.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response('search_contact.html', {
        'results': results,
        'query': query,
    })


    # def contact_list(request, agendaId):
    # agenda = get_object_or_404(Agenda, id = agendaId)
    # contactos = agenda.contactos.all()
    # context = {'contactos': contactos, 'agendaId': agendaId}
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