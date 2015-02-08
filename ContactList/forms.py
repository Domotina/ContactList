from django.forms import ModelForm
from django import forms

from .models import ContactList, Contact, Company, Location, LocationData, SocialNetwork


class ContactListForm(ModelForm):
    class Meta:
        model = ContactList
        exclude = ('owner_list', )

    def save(self, commit=True, owner_list=None):
        if not self.instance.pk:
            if not owner_list:
                raise TypeError("Owner is required to create a Contact List.")
            self.instance.owner_list = owner_list
        return super(ContactListForm, self).save(commit)


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        exclude = ('contact_list',)

    def save(self, commit=True, contact_list=None):
        if not self.instance.pk:
            if not contact_list:
                raise TypeError("Contact List is required to create a Contact.")
            self.instance.contact_list = contact_list
        return super(ContactForm, self).save(commit)

class CompanyForm(ModelForm):
    class Meta:
        model = Company

class LocationForm(ModelForm):
    class Meta:
        model = Location
        exclude = ('owner_contact', )

    def save(self, commit=True, owner_contact=None):
        if not self.instance.pk:
            if not owner_contact:
                raise TypeError("Contact is required to create a Location.")
            self.instance.owner_contact = owner_contact
        return super(LocationForm, self).save(commit)


class SocialNetworkForm(ModelForm):
    class Meta:
        model = SocialNetwork
        exclude = ('owner', )

    def save(self, commit=True, owner=None):
        if not self.instance.pk:
            if not owner:
                raise TypeError("Contact is required to create a Social Network account.")
            self.instance.owner = owner
        return super(SocialNetworkForm, self).save(commit)


class LocationDataForm(ModelForm):
    class Meta:
        model = LocationData

class SearchForm(ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)

    class Meta:
        model = Contact


