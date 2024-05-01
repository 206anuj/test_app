from django.db import models

# Create your models here.

from django.db import models

class NewData1(models.Model):
    id = models.AutoField(primary_key=True)
    attributes = models.TextField(blank=True, null=True)
    country1_c = models.TextField(db_column='country1__c', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    city_c = models.TextField(db_column='city__c', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    projectname = models.TextField(blank=True, null=True)
    skill_level_c = models.TextField(db_column='skill_level__c', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    currencyisocode = models.TextField(blank=True, null=True)
    region_c = models.TextField(db_column='region__c', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    sourced_by_c = models.TextField(db_column='sourced_by__c', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    project_c = models.TextField(db_column='project__c', blank=True, null=True)  # Field renamed because it contained more than one '_' in a row.
    customername = models.TextField(blank=True, null=True)
    vendorproject = models.TextField(blank=True, null=True)
    vendorname = models.TextField(blank=True, null=True)
    minmonthrate = models.TextField(blank=True, null=True)
    maxmonthrate = models.TextField(blank=True, null=True)
    minvendorrate = models.TextField(blank=True, null=True)
    maxvendorrate = models.TextField(blank=True, null=True)
    avgmonthlyrate = models.TextField(blank=True, null=True)
    avgvendorrate = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.id) + ' ' + str(self.projectname)
