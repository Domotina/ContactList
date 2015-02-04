from django.forms import ModelForm
from django import forms

from .models import ContactList, Contact, Company, Location, LocationData

class ContactListForm(ModelForm):
    class Meta:
        model = ContactList
        exclude = ('owner_list',)

    def save(self, commit=True, owner_list=None):
        if not self.instance.pk:
            if not owner_list:
                raise TypeError("Owner is required to create a Contact List.")
            self.instance.owner_list = owner_list
        return super(ContactListForm, self).save(commit)


class ContactForm(ModelForm):
    class Meta:
        model = Contact

class CompanyForm(ModelForm):
    class Meta:
        model = Company

class LocationForm(ModelForm):
    class Meta:
        model = Location

class LocationDataForm(ModelForm):
    class Meta:
        model = LocationData

class SearchForm(ModelForm):
    name = forms.CharField(label='Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)

