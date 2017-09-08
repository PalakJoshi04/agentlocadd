from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class Agent(models.Model):
    agent_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    education = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    specialization = models.CharField(max_length=100)
    experence = models.IntegerField()
    agent_notes = models.TextField()


    def get_absolute_url(self):
        return reverse('agent-update', kwargs={'pk': self.pk})

class Location(models.Model):
    agent = models.ForeignKey(Agent)
    foreign_id = models.AutoField(primary_key=True)
    location_name = models.CharField(max_length=50)
    city = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)

class Address(models.Model):
    agent = models.ForeignKey(Agent)
    address_id = models.AutoField(primary_key=True)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    landmark = models.CharField(max_length=20)
    pincode = models.IntegerField()