from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.template import RequestContext
from django.db.models import Q

from .forms import ContactListForm, ContactForm, CompanyForm, SearchForm, LocationForm, SocialNetworkForm
from .models import ContactList, Contact, Location, SocialNetwork


def home(request):
    contact_lists = ContactList.public.all()
    context = {'contact_lists': contact_lists}
    return render(request, 'index.html', context)


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
        contact_lists = ContactList.public.filter(owner__username=username)
    context = {'contact_lists': contact_lists, 'owner': user}
    return render(request, 'contact_list_user.html', context)


@login_required
def contact_list_create(request):
    if request.method == 'POST':
        form = ContactListForm(data=request.POST)
        if form.is_valid():
            form.save(owner=request.user)
            return redirect('app_contact_list_user', username=request.user.username)
    else:
        form = ContactListForm()
    return render(request, 'form.html', {'form': form, 'create': True, 'object': 'contact list'})


@login_required
def contact_list_edit(request, pk):
    contact_list = get_object_or_404(ContactList, pk=pk)
    if contact_list.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = ContactListForm(instance=contact_list, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_contact_list_user', username=request.user.username)
    else:
        form = ContactListForm(instance=contact_list)
    return render(request, 'form.html',
                  {'form': form, 'create': False, 'object': 'contact list', 'contact_list': contact_list})


@login_required
def contacts(request, contact_list_id):
    contact_list = get_object_or_404(ContactList, id=contact_list_id)
    contacts = Contact.objects.filter(contact_list=contact_list)
    context = {'contacts': contacts, 'contact_list': contact_list}
    # print context
    return render(request, 'contacts.html', context)


@login_required
def contact_create(request, contact_list_id):
    contact_list = get_object_or_404(ContactList, id=contact_list_id)
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            form.save(contact_list=contact_list)
            return redirect('app_contacts', contact_list_id=contact_list_id)
    else:
        form = ContactForm()
    return render(request, 'form.html', {'form': form, 'create': True, 'object': 'contact'})


@login_required
def contact_edit(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if contact.contact_list.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = ContactForm(instance=contact, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_contacts', contact_list_id=contact.contact_list.id)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'form.html', {'form': form, 'create': False, 'object': 'contact', 'contact': contact})


@login_required
def locations(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    locations = Location.objects.filter(contact=contact)
    context = {'locations': locations, 'contact': contact}
    return render(request, 'locations.html', context)


@login_required
def location_create(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = LocationForm(data=request.POST)
        if form.is_valid():
            form.save(contact=contact)
            return redirect('app_locations', contact_id=contact_id)
    else:
        form = LocationForm()
    return render(request, 'form.html', {'form': form, 'create': True, 'object': 'location'})


@login_required
def location_edit(request, pk):
    location = get_object_or_404(Location, pk=pk)
    if location.contact.contact_list.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = LocationForm(instance=location, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_locations', contact_id=location.contact.id)
    else:
        form = LocationForm(instance=location)
    return render(request, 'form.html', {'form': form, 'create': False, 'object': 'location', 'location': location})


@login_required
def social_networks(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    social_networks = SocialNetwork.objects.filter(owner=contact)
    context = {'social_networks': social_networks, 'contact': contact}
    return render(request, 'social_networks.html', context)


@login_required
def social_network_create(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == 'POST':
        form = SocialNetworkForm(data=request.POST)
        if form.is_valid():
            form.save(owner=contact)
            return redirect('app_social_networks', contact_id=contact_id)
    else:
        form = SocialNetworkForm()
    return render(request, 'form.html', {'form': form, 'create': True, 'object': 'social network'})


@login_required
def social_network_edit(request, pk):
    social_network = get_object_or_404(SocialNetwork, pk=pk)
    if social_network.owner.contact_list.owner != request.user and not request.user.is_superuser:
        raise PermissionDenied
    if request.method == 'POST':
        form = SocialNetworkForm(instance=social_network, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_social_networks', contact_id=social_network.owner.id)
    else:
        form = SocialNetworkForm(instance=social_network)
    return render(request, 'form.html',
                  {'form': form, 'create': False, 'object': 'social network', 'social_network': social_network})


@login_required
def company_create(request, contact_list_id):
    if request.method == 'POST':
        form = CompanyForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('app_contacts', contact_list_id=contact_list_id)
    else:
        form = CompanyForm()
    return render(request, 'form.html', {'form': form, 'create': True, 'object': 'company'})


# def go_to_search(request):
# if request.method == 'GET':
# form = SearchForm(data=request.GET)
# if form.is_valid():
#             print (form)
#             print(request.GET.get('name'))
#             return redirect('app_search', name = "Cindy")
#     else:
#         form = SearchForm()
#     return render(request, 'search_contact.html', {'data': False, 'form': form})

def search(request):
    print('Entro')
    if 'name' in request.GET and request.GET['name']:
        search_name = request.GET['name']
        print request.GET['name']
        contacts = Contact.objects.filter(Q(first_name__icontains=search_name))
        context = {'data': True, 'contacts': contacts}
        return render(request, 'search_contact.html', context)
    else:
        contacts = []

    if 'last_name' in request.GET and request.GET['last_name']:
        search_last_name = request.GET['last_name']
        print request.GET['last_name']
        contacts = Contact.objects.filter(Q(last_name__icontains=search_last_name))
        context = {'data': True, 'contacts': contacts}
        return render(request, 'search_contact.html', context)
    else:
        contacts = []

    context = {'data': True, 'contacts': contacts}
    return render(request, 'search_contact.html', context)
