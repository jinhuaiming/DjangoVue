from django.db import models


# Create your models here.


class Argofloat(models.Model):
    platformnumber = models.IntegerField(primary_key=True)
    datecenter = models.TextField(blank=True, null=True)
    lauchdate = models.CharField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=5, decimal_places=3, blank=True, null=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    projectname = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'argofloat'
        db_table_comment = '01 Argo-浮标基础信息表'


class Argoheader(models.Model):
    platformnumber = models.IntegerField(
        primary_key=True)  # The composite primary key (platformnumber, cyclenumber) found, that is not supported. The first column is selected.
    cyclenumber = models.IntegerField()
    julianday = models.CharField(blank=True, null=True)
    datadate = models.CharField(blank=True, null=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    longitude = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'argoheader'
        unique_together = (('platformnumber', 'cyclenumber'),)
        db_table_comment = '03 Argo-观测次数信息表'


class Argocore(models.Model):
    platformnumber = models.IntegerField(
        primary_key=True)  # The composite primary key (platformnumber, cyclenumber, pressure) found, that is not supported. The first column is selected.
    cyclenumber = models.IntegerField()
    pressure = models.DecimalField(max_digits=7, decimal_places=1)
    cpressure = models.DecimalField(max_digits=7, decimal_places=1, blank=True, null=True)
    qpressure = models.CharField(max_length=1, blank=True, null=True)
    temperature = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    ctemperature = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    qtemperature = models.CharField(max_length=1, blank=True, null=True)
    salinity = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    csalinity = models.DecimalField(max_digits=9, decimal_places=3, blank=True, null=True)
    qsalinity = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'argocore'
        unique_together = (('platformnumber', 'cyclenumber', 'pressure'),)
        db_table_comment = '02 Argo-核心数据表'
