from django.db import models

"""
# Create your models here.
class Dimforecastkpi(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=45, blank=True, null=True)  # Field name made lowercase.
    measunit = models.CharField(db_column='MeasUnit', max_length=45, blank=True, null=True)  # Field name made lowercase.
    horizon = models.IntegerField(db_column='Horizon', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimForecastKPI'


class Dimlocation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    latitude = models.FloatField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase.
    longitude = models.FloatField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimLocation'


class Dimmeasurementunit(models.Model):
    id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    measname = models.TextField(db_column='MeasName', blank=True, null=True)  # Field name made lowercase.
    measunit = models.TextField(db_column='MeasUnit', blank=True, null=True)  # Field name made lowercase.
    measunitdesc = models.TextField(db_column='MeasUnitDesc', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimMeasurementUnit'


class Dimmeteoforecastlog(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    meteodataproviderid = models.IntegerField(db_column='MeteoDataProviderID')  # Field name made lowercase.
    startdatemeteoforecastdata = models.TextField(db_column='StartDateMeteoForecastData')  # Field name made lowercase.
    enddatemeteoforecastdata = models.TextField(db_column='EndDateMeteoForecastData')  # Field name made lowercase.
    meteoforecastdataacquisitiondate = models.TextField(db_column='MeteoForecastDataAcquisitionDate', blank=True, null=True)  # Field name made lowercase.
    meteoforecastdatastatus = models.TextField(db_column='MeteoForecastDataStatus', blank=True, null=True)  # Field name made lowercase.
    meteoforecastdatastatusnotes = models.TextField(db_column='MeteoForecastDataStatusNotes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimMeteoForecastLog'


class Dimproductiontypeemie(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    productiontypetext = models.CharField(db_column='ProductionTypeText', max_length=45, blank=True, null=True)  # Field name made lowercase.
    entitycreated = models.DateTimeField(db_column='EntityCreated', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimProductionTypeEmie'


class Dimresarea(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    arearefid = models.IntegerField(db_column='AreaRefID', blank=True, null=True)  # Field name made lowercase.
    productiontypeemieid = models.IntegerField(db_column='ProductionTypeEmieID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimRESArea'


class Dimresgenforecastlog(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    serviceid = models.IntegerField(db_column='ServiceID', blank=True, null=True)  # Field name made lowercase.
    startdateforecast = models.TextField(db_column='StartDateForecast', blank=True, null=True)  # Field name made lowercase.
    enddateforecast = models.TextField(db_column='EndDateForecast', blank=True, null=True)  # Field name made lowercase.
    meteoforecastacquisitiondate = models.TextField(db_column='MeteoForecastAcquisitionDate', blank=True, null=True)  # Field name made lowercase.
    runningservicedatetime = models.TextField(db_column='RunningServiceDateTime', blank=True, null=True)  # Field name made lowercase.
    servicestatus = models.CharField(db_column='ServiceStatus', max_length=200, blank=True, null=True)  # Field name made lowercase.
    servicestatusnotes = models.CharField(db_column='ServiceStatusNotes', max_length=450, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimRESGenForecastLog'

"""
class Dimresgenforecastmodel(models.Model):
    modelid = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    desc = models.TextField(db_column='Desc', blank=True, null=True)  # Field name made lowercase.
    productiontypeemieid = models.IntegerField(db_column='ProductionTypeEmieID', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimRESGenForecastModel'


"""
class Dimresgenforecastservice(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    resid = models.IntegerField(db_column='RESID', blank=True, null=True)  # Field name made lowercase.
    reslevel = models.CharField(db_column='RESLevel', max_length=45, blank=True, null=True)  # Field name made lowercase.
    productiontypeemieid = models.IntegerField(db_column='ProductionTypeEmieID', blank=True, null=True)  # Field name made lowercase.
    marketsegment = models.TextField(db_column='MarketSegment', blank=True, null=True)  # Field name made lowercase.
    modelid = models.TextField(db_column='ModelID', blank=True, null=True)  # Field name made lowercase.
    horizon = models.IntegerField(db_column='Horizon', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimRESGenForecastService'


class Factinstalledcapacity(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    arearefid = models.IntegerField(db_column='AreaRefID', blank=True, null=True)  # Field name made lowercase.
    datetime = models.DateTimeField(db_column='DateTime', blank=True, null=True)  # Field name made lowercase.
    productiontypeemieid = models.IntegerField(db_column='ProductionTypeEmieID', blank=True, null=True)  # Field name made lowercase.
    installedcapacity = models.FloatField(db_column='InstalledCapacity', blank=True, null=True)  # Field name made lowercase.
    generatedenergy = models.FloatField(db_column='GeneratedEnergy', blank=True, null=True)  # Field name made lowercase.
    resolutioncode = models.CharField(db_column='ResolutionCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fetchevent = models.CharField(db_column='FetchEvent', max_length=250, blank=True, null=True)  # Field name made lowercase.
    updatedatetime = models.DateTimeField(db_column='UpdateDateTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FactInstalledCapacity'


class Factmeteoforecast(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    meteoforecastlogid = models.BigIntegerField(db_column='MeteoForecastLogID', blank=True, null=True)  # Field name made lowercase.
    timestamp_utc = models.TextField(db_column='Timestamp_UTC', blank=True, null=True)  # Field name made lowercase.
    u = models.FloatField(db_column='U', blank=True, null=True)  # Field name made lowercase.
    v = models.FloatField(db_column='V', blank=True, null=True)  # Field name made lowercase.
    temperature = models.FloatField(db_column='Temperature', blank=True, null=True)  # Field name made lowercase.
    humidity = models.FloatField(db_column='Humidity', blank=True, null=True)  # Field name made lowercase.
    cloudcover = models.FloatField(db_column='CloudCover', blank=True, null=True)  # Field name made lowercase.
    wspeed = models.FloatField(db_column='WSpeed', blank=True, null=True)  # Field name made lowercase.
    wdir = models.FloatField(db_column='WDir', blank=True, null=True)  # Field name made lowercase.
    solarradiation = models.FloatField(db_column='SolarRadiation', blank=True, null=True)  # Field name made lowercase.
    locationid = models.BigIntegerField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FactMeteoForecast'


class Factresgenforecastdata(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    resgenforecastlogid = models.IntegerField(db_column='RESGenForecastLogID')  # Field name made lowercase.
    time_index = models.IntegerField(db_column='Time_index')  # Field name made lowercase.
    ts_created = models.DateTimeField(db_column='TS_created')  # Field name made lowercase.
    powerpredict = models.FloatField(db_column='PowerPredict', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FactRESGenForecastData'


class FactresgenforecastdataHistorical(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    resgenforecastlogid = models.IntegerField(db_column='RESGenForecastLogID')  # Field name made lowercase.
    time_index = models.IntegerField(db_column='Time_index')  # Field name made lowercase.
    ts_created = models.DateTimeField(db_column='TS_created')  # Field name made lowercase.
    powerpredict = models.FloatField(db_column='PowerPredict', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FactRESGenForecastData_Historical'


class Factresgenforecastevaluation(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    resgenforecastlogid = models.IntegerField(db_column='RESGenForecastLogID', blank=True, null=True)  # Field name made lowercase.
    eval_timestamp = models.DateTimeField(db_column='Eval_Timestamp', blank=True, null=True)  # Field name made lowercase.
    forecastprovider = models.CharField(db_column='ForecastProvider', max_length=45, blank=True, null=True)  # Field name made lowercase.
    actualprovider = models.CharField(db_column='ActualProvider', max_length=45, blank=True, null=True)  # Field name made lowercase.
    kpi_id = models.IntegerField(db_column='KPI_ID', blank=True, null=True)  # Field name made lowercase.
    value = models.FloatField(db_column='Value', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FactRESGenForecastEvaluation'
"""