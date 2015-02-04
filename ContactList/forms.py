from django.forms import ModelForm

from .models import ContactList

class ContactListForm(ModelForm):
    class Meta:
        model = ContactList
        exclude = ('owner_list',)

    def save(self, commit = True, owner_list = None):
        if not self.instance.pk:
            if not owner_list:
                raise TypeError("Owner is required to create a Contact List.")
            self.instance.owner_list = owner_list
        return super(ContactListForm, self).save(commit)