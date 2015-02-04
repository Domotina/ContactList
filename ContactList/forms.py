from django.forms import ModelForm

from .models import ContactList, Contact, Company

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
        exclude = ('contact_list',)

    def save(self, commit=True, contact_list=None):
        if not self.instance.pk:
            if not contact_list:
                raise TypeError("Contact_List is required to create a Contact.")
            self.instance.contact_list = contact_list
        return super(ContactForm, self).save(commit)

class CompanyForm(ModelForm):
    class Meta:
        model = Company