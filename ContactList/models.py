from django.db import models
from django.contrib.auth.models import User

from django.utils.timezone import now

class Contacto(models.Model):
    nombres = models.CharField(max_length = 50)
    apellidos = models.CharField(max_length = 50)
    empresa = models.CharField(max_length = 100)

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'
        ordering = ['-apellidos']

    def __str__(self):
        return '%s %s' % (self.nombres, self.apellidos)


class PublicAgendaManager(models.Manager):
    def get_queryset(self):
        qs = super(PublicAgendaManager, self).get_queryset()
        return qs.filter(es_publico = True)


class Agenda(models.Model):
    nombre = models.CharField('name', max_length = 50)
    es_publico = models.BooleanField('public', default = True)
    propietario = models.ForeignKey(User, verbose_name = "propietario", related_name = "agendas")
    fecha_creacion = models.DateTimeField('date created')
    fecha_modificacion = models.DateTimeField('date updated')
    contactos = models.ManyToManyField(Contacto, blank = True)

    objects = models.Manager()
    public = PublicAgendaManager()

    class Meta:
        verbose_name = 'agenda'
        verbose_name_plural = 'agendas'
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.nombre

    def save(self, *args, **kwargs):
        if not self.id:
            self.fecha_creacion = now()

        self.fecha_modificacion = now()
        super(Agenda, self).save(*args, **kwargs)
