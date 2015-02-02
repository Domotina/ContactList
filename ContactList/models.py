# Importation of models
from django.db import models
# Importation of User model from Django authentication framework.
from django.contrib.auth.models import User

class Company(models.Model):
    name_company = models.CharField('name_company',max_length=100)
    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'
        ordering = ['name_company']

    def __unicode__(self):
        return '%s' % self.name_company


class TypeData(models.Model):

    type_data = models.CharField('type_data',max_length=50)

    class Meta:
        ordering = ['type_data']

    def __unicode__(self):
        return '%s' % self.type_data


class Contact_list(models.Model):

    name_list = models.CharField('name_list',max_length=100)
    owner_list = models.ForeignKey(User)

    class Meta:
        verbose_name = 'contact_list'
        verbose_name_plural = 'contact_lists'
        ordering = ['name_list']

    def __unicode__(self):
        return '%s' % self.name_list

class Contact(models.Model):
    first_name = models.CharField('first_name',max_length=50)
    second_name = models.CharField('second_name',max_length=50)
    last_name = models.CharField('last_name',max_length=50)
    contact_company = models.ForeignKey(Company,blank=True,null=True)
    contact_list = models.ForeignKey(Contact_list)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ['last_name']

    def __unicode__(self):
        return '%s' % self.last_name+' '+self.first_name+' '+self.second_name


class Location(models.Model):
    location = models.CharField('location',max_length=255)
    owner_contact = models.ForeignKey(Contact)

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'
        ordering = ['location']

    def __unicode__(self):
        return '%s' % self.location

class LocationData(models.Model):

    location_data = models.CharField('type',max_length=255)
    location_reference = models.ForeignKey(Location)
    type_data = models.ForeignKey(TypeData)

    class Meta:
        verbose_name = 'location_data'
        verbose_name_plural = 'locations_data'

    def __unicode__(self):
        return '%s' % self.type_data+': '+self.location_data




# class Contacto(models.Model):
#     nombres = models.CharField('name', max_length = 50)
#     apellidos = models.CharField('last name', max_length = 50)
#     empresa = models.CharField('working place', max_length = 100)
#
#     class Meta:
#         verbose_name = 'contact'
#         verbose_name_plural = 'contacts'
#         ordering = ['-apellidos']
#
#     def __str__(self):
#         return '%s %s' % (self.nombres, self.apellidos)
#
#
# class PublicAgendaManager(models.Manager):
#     def get_queryset(self):
#         qs = super(PublicAgendaManager, self).get_queryset()
#         return qs.filter(es_publico = True)
#
#
# class Agenda(models.Model):
#     nombre = models.CharField('name', max_length = 50)
#     es_publico = models.BooleanField('public', default = True)
#     propietario = models.ForeignKey(User, verbose_name = "propietario", related_name = "agendas")
#     fecha_creacion = models.DateTimeField('date created')
#     fecha_modificacion = models.DateTimeField('date updated')
#     contactos = models.ManyToManyField(Contacto, blank = True)
#
#     objects = models.Manager()
#     public = PublicAgendaManager()
#
#     class Meta:
#         verbose_name = 'agenda'
#         verbose_name_plural = 'agendas'
#         ordering = ['-fecha_creacion']
#
#     def __str__(self):
#         return self.nombre
#
#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.fecha_creacion = now()
#
#         self.fecha_modificacion = now()
#         super(Agenda, self).save(*args, **kwargs)
