from django.db import models

#Model CRUD
class List(models.Model):
    owner = models.CharField(max_length=60)
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class Company(models.Model):
    name_company = models.CharField(max_length=50)


class Contact(models.Model):
    name_contact = models.CharField(max_length=50)
    last_name_contact = models.CharField(max_length=50)
    notebook_contact = models.ForeignKey('List', db_column='List_id')
    company_contact = models.ForeignKey('Company', db_column='Company_id')


class Location(models.Model):
    name_location = models.CharField(max_length=50)
    contact_location = models.ForeignKey('Contact', db_column='Contact_id')


class Phone(models.Model):
    indicative = models.CharField(max_length=5)
    number = models.IntegerField(max_length=15)
    location_phone = models.ForeignKey('Location', db_column='Location_id')


class Address(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    location_address = models.ForeignKey('Location', db_column='Location_id')


class Email(models.Model):
    email = models.CharField(max_length=50)
    location_email = models.ForeignKey('Location', db_column='Location_id')