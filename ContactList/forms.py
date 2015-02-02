from django.forms import ModelForm

from .models import Agenda, Contacto


class AgendaForm(ModelForm):
    class Meta:
        model = Agenda
        exclude = ('fecha_creacion', 'fecha_modificacion', 'propietario', 'contactos')

    def save(self, commit = True, propietario = None):
        if not self.instance.pk:
            if not propietario:
                raise TypeError("Propietario is required to create an Agenda.")
            self.instance.propietario = propietario
        return super(AgendaForm, self).save(commit)

class ContactoForm(ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombres', 'apellidos', 'empresa']