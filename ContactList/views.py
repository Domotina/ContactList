from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.template import RequestContext
from django.db.models import Q

from .forms import ContactListForm, ContactForm, CompanyForm, SearchForm, LocationDataForm, LocationForm
from .models import ContactList, Contact, Location, LocationData


def contact_lists(request):
    if request.user.is_authenticated:
        contact_lists = ContactList.objects.all()
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
    return render(request, 'form.html', {'form': form, 'create': True, 'object': 'contact list'})


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
    return render(request, 'form.html', {'form': form, 'create': False, 'object': 'contact list', 'contact_list': contact_list})


@login_required
def contacts(request, contactListId):
    contactList = get_object_or_404(ContactList, id = contactListId)
    contacts = Contact.objects.filter(contact_list = contactList)
    context = {'contacts': contacts, 'contactListId': contactListId, 'contactList': contactList}
    return render(request, 'contacts.html', context)


@login_required
def contact_create(request, contactListId):
    contactList = get_object_or_404(ContactList, id = contactListId)
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        if form.is_valid():
            form.save(contact_list=contactList)
            return redirect('app_contacts', contactListId = contactListId)
    else:
        form = ContactForm()
    return render(request, 'form.html', {'form': form, 'create': True, 'object': 'contact'})


@login_required
def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if contact.contact_list.owner_list != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = ContactForm(instance=contact, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_contacts', contactListId = contact.contact_list.id)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'form.html', {'form': form, 'create': False, 'object': 'contact', 'contact': contact})


@login_required
def locations(request, contactId):
    contact = get_object_or_404(Contact, id = contactId)
    print contact
    locations = Location.objects.filter(owner_contact = contact)
    print locations
    context = {'locations': locations, 'contactId': contactId, 'contact': contact}
    return render(request, 'locations.html', context)


@login_required
def location_create(request, contactId):
    contact = get_object_or_404(Contact, id = contactId)
    if request.method == 'POST':
        form = LocationForm(data = request.POST)
        if form.is_valid():
            form.save(owner_contact=contact)
            print(contactId)
            return redirect('app_locations', contactId = contactId)
    else:
        form = LocationForm()
    return render(request, 'form.html', {'form': form, 'create': True, 'object': 'location'})


@login_required
def location_edit(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if location.contact.contact_list.owner_list != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = LocationForm(instance=location, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_locations', contactId = location.contact.id)
    else:
        form = LocationForm(instance=location)
    return render(request, 'form.html', {'form': form, 'create': False, 'object': 'location', 'location': location})



def app_contact_list_contact(request, pk):
    try:
        # Ojo hay que validar bien
        contacts = Contact.objects.all()
        print contacts
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
            #return redirect('../viewContacts/' + str(form.instance.contact_list.id))
            print "ContactList.id"
            print str(form.instance.contact_list.id)
            return redirect('app_contact_list_contact', str(form.instance.contact_list.id))

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