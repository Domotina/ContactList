from django import forms
from ContactList.models import Address, Company, Contact, Email, List, Location, Phone

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        widgets = {
            'password': forms.PasswordInput(),
        }

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
