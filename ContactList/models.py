# Importation of models
from django.db import models
# Importation of User model from Django authentication framework.
from django.contrib.auth.models import User
from django.conf import settings

class Company(models.Model):
    name_company = models.CharField('Name',max_length=100)
    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'
        ordering = ['name_company']

    def __unicode__(self):
        return '%s' % self.name_company


class TypeData(models.Model):

    type_data = models.CharField('Type Data',max_length=50)

    class Meta:
        ordering = ['type_data']

    def __unicode__(self):
        return '%s' % self.type_data


class PublicContactListManager(models.Manager):
    def get_queryset(self):
        qs = super(PublicContactListManager, self).get_queryset()
        return qs.filter(is_public = True)

class ContactList(models.Model):

    name_list = models.CharField('Name',max_length=100)
    #owner_list = models.ForeignKey(User, verbose_name = "owner_list", related_name = "contact_lists")
    is_public = models.BooleanField('public', default = True)

    objects = models.Manager()
    public = PublicContactListManager()

    class Meta:
        verbose_name = 'contact_list'
        verbose_name_plural = 'contact_lists'
        ordering = ['name_list']

    def __unicode__(self):
        return '%s' % self.name_list

class Collaborator(models.Model):
    contactList = models.ForeignKey(ContactList, related_name="collaborators")
    username = models.ForeignKey(User, verbose_name = "username", related_name = "collaborators")
    is_owner = models.BooleanField('Is Owner',default=False)

class Contact(models.Model):
    first_name = models.CharField('First Name', max_length=50)
    second_name = models.CharField('Middle Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    contact_company = models.ForeignKey(Company, blank=True, null=True)
    contact_list = models.ForeignKey(ContactList)

    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ['last_name']

    def __unicode__(self):
        return '%s' % self.last_name+' '+self.first_name+' '+self.second_name

class SocialNetworkType(models.Model):
    name = models.CharField('Social Network', max_length=50)
    icon = models.ImageField('Icon Image', upload_to=settings.UPLOADED_FILE_PATH)

    class Meta:
        verbose_name = 'social network type'
        verbose_name_plural = 'social network types'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class SocialNetwork(models.Model):
    type = models.ForeignKey(SocialNetworkType)
    url = models.CharField('Link', max_length=200)
    owner = models.ForeignKey(Contact)

    class Meta:
        verbose_name = 'social network'
        verbose_name_plural = 'social networks'

    def __unicode__(self):
        return '%s %s' % (self.name, self.url)

class LocationData(models.Model):

    location_data = models.CharField('type',max_length=255)

    def __unicode__(self):
        return '%s' % self.location_data


class Location(models.Model):
    informacion = models.CharField('Location Information',max_length=255)
    tipo = models.ForeignKey(TypeData)
    location = models.ForeignKey(LocationData)

    owner_contact = models.ForeignKey(Contact)

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'
        ordering = ['location']

    def __unicode__(self):
        return '%s' % self.location
