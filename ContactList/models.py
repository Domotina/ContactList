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


class PublicContactListManager(models.Manager):
    def get_queryset(self):
        qs = super(PublicContactListManager, self).get_queryset()
        return qs.filter(is_public = True)

class ContactList(models.Model):

    name_list = models.CharField('name list',max_length=100)
    owner_list = models.ForeignKey(User, verbose_name = "owner_list", related_name = "contact_lists")
    is_public = models.BooleanField('public', default = True)

    objects = models.Manager()
    public = PublicContactListManager()

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
    facebook = models.CharField('Facebook',max_length=100)
    google = models.CharField('Google+',max_length=100)
    twitter = models.CharField('Twitter',max_length=100)
    contact_company = models.ForeignKey(Company,blank=True,null=True)
    contact_list = models.ForeignKey(ContactList)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ['last_name']

    def __unicode__(self):
        return '%s' % self.last_name+' '+self.first_name+' '+self.second_name

class LocationData(models.Model):

    location_data = models.CharField('type',max_length=255)

    def __unicode__(self):
        return '%s' % self.location_data


class Location(models.Model):
    informacion = models.CharField('contact information',max_length=255)
    tipo = models.ForeignKey(TypeData)
    location = models.ForeignKey(LocationData)

    owner_contact = models.ForeignKey(Contact)

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'
        ordering = ['location']

    def __unicode__(self):
        return '%s' % self.location

