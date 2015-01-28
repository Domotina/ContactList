from django.shortcuts import HttpResponseRedirect, render_to_response, render
from django.template import RequestContext
from ContactList.models import Contact
from ContactList.forms import CompanyForm, ListForm, ContactForm, LocationForm, AddressForm, EmailForm, PhoneForm

# Create your views here.


def index(request):
    contacts = Contact.objects.all().order_by('name_contact')
    return render_to_response('index.html', {"contacts": contacts}, context_instance=RequestContext(request))

def create(request):
    return render_to_response("homeViewTemplate.html", locals(), context_instance=RequestContext(request))

def CompanyView(request):

    form = CompanyForm(request.POST or None)
    entity = "Company"

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    return render_to_response("formTemplate.html", locals(), context_instance=RequestContext(request))

def ListView(request):

    form = ListForm(request.POST or None)
    entity = "List"

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    return render_to_response("formTemplate.html", locals(), context_instance=RequestContext(request))

def ContactView(request):

    form = ContactForm(request.POST or None)
    entity = "Contact"

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    return render_to_response("formTemplate.html", locals(), context_instance=RequestContext(request))

def LocationView(request):

    form = LocationForm(request.POST or None)
    entity = "Location"

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    return render_to_response("formTemplate.html", locals(), context_instance=RequestContext(request))

def AddressView(request):

    form = AddressForm(request.POST or None)
    entity = "Address"

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    return render_to_response("formTemplate.html", locals(), context_instance=RequestContext(request))

def EmailView(request):

    form = EmailForm(request.POST or None)
    entity = "Email"

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    return render_to_response("formTemplate.html", locals(), context_instance=RequestContext(request))

def PhoneView(request):

    form = PhoneForm(request.POST or None)
    entity = "Phone"

    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    return render_to_response("formTemplate.html", locals(), context_instance=RequestContext(request))
