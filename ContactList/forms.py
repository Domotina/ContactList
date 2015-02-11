from django.forms import ModelForm
from django import forms

from .models import ContactList, Collaborator, Contact, Company, Location, SocialNetwork


class ContactListForm(ModelForm):
    class Meta:
        model = ContactList
        exclude = ('owner', )

    def save(self, commit=True, owner=None):
        if not self.instance.pk:
            if not owner:
                raise TypeError("Owner is required to create a Contact List.")
            self.instance.owner = owner
        return super(ContactListForm, self).save(commit)


class CollaboratorForm(ModelForm):
    class Meta:
        model = Collaborator
        exclude = ('contact_list', )

    def save(self, commit=True, contact_list=None):
        if not self.instance.pk:
            if not contact_list:
                raise TypeError("Contact list is required to create a Collaborator.")
            self.instance.contact_list = contact_list
        return super(CollaboratorForm, self).save(commit)


class CompanyForm(ModelForm):
    class Meta:
        model = Company


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


class LocationForm(ModelForm):
    class Meta:
        model = Location
        exclude = ('contact', )

    def save(self, commit=True, contact=None):
        if not self.instance.pk:
            if not contact:
                raise TypeError("Contact is required to create a Location.")
            self.instance.contact = contact
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


class SearchForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=False)
    last_name = forms.CharField(label='Last Name', max_length=100, required=False)

