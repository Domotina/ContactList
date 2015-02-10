# Importation of models
from django.db import models
# Importation of User model from Django authentication framework.
from django.contrib.auth.models import User
from django.conf import settings


class Company(models.Model):
    name = models.CharField('name',max_length=100)
    class Meta:
        verbose_name = 'company'
        verbose_name_plural = 'companies'
        ordering = ['name']

    def __unicode__(self):
        return '%s' % self.name


class PublicContactListManager(models.Manager):
    def get_queryset(self):
        qs = super(PublicContactListManager, self).get_queryset()
        return qs.filter(is_public = True)

class ThemeContactList(models.Model):
    theme = models.CharField('theme',max_length=100)
    file_theme = models.CharField('file',max_length=100)

    def __unicode__(self):
        return self.theme

class ContactList(models.Model):
    name = models.CharField('name',max_length=100)
    owner = models.ForeignKey(User, verbose_name = "owner", related_name = "contact_lists")
    is_public = models.BooleanField('public', default = True)
    theme = models.ForeignKey(ThemeContactList,verbose_name='theme')
    objects = models.Manager()
    public = PublicContactListManager()
    class Meta:
        verbose_name = 'contact list'
        verbose_name_plural = 'contact lists'
        ordering = ['name']

    def __unicode__(self):
        return '%s' % self.name


class Contact(models.Model):
    first_name = models.CharField('first name', max_length=50)
    middle_name = models.CharField('middle name', max_length=50, blank=True, null=True)
    last_name = models.CharField('last name', max_length=50)
    company = models.ForeignKey(Company, blank=True, null=True)
    contact_list = models.ForeignKey(ContactList)
    class Meta:
        verbose_name = 'contact'
        verbose_name_plural = 'contacts'
        ordering = ['last_name']

    def __unicode__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.middle_name)


class SocialNetworkType(models.Model):
    name = models.CharField('social network', max_length=50)
    icon = models.ImageField('icon image', upload_to=settings.UPLOADED_FILE_PATH)
    class Meta:
        verbose_name = 'social network type'
        verbose_name_plural = 'social network types'
        ordering = ['name']

    def __unicode__(self):
        return self.name


class SocialNetwork(models.Model):
    type = models.ForeignKey(SocialNetworkType)
    url = models.CharField('link', max_length=200)
    owner = models.ForeignKey(Contact)
    class Meta:
        verbose_name = 'social network'
        verbose_name_plural = 'social networks'

    def __unicode__(self):
        return '%s %s' % (self.name, self.url)


class LocationType(models.Model):
    name = models.CharField('type', max_length=50)
    class Meta:
        verbose_name = 'location type'
        verbose_name_plural = 'location types'
        ordering = ['name']

    def __unicode__(self):
        return '%s' % self.name


class LocationPlace(models.Model):
    name = models.CharField('place',max_length=255)
    class Meta:
        verbose_name = 'location place'
        verbose_name_plural = 'location places'
        ordering = ['name']

    def __unicode__(self):
        return '%s' % self.name


class Location(models.Model):
    info = models.CharField('location',max_length=255)
    type = models.ForeignKey(LocationType)
    place = models.ForeignKey(LocationPlace)
    contact = models.ForeignKey(Contact)
    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'
        ordering = ['type']

    def __unicode__(self):
        return '%s - %s: %s' % (self.type, self.location, self.info)
