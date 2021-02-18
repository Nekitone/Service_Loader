from django.db import models

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

"""
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
    id = models.IntegerField(db_column='ID', blank=True, primary_key=True)  # Field name made lowercase.
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


class Dimpvcluster(models.Model):
    psid = models.IntegerField(db_column='PSID', blank=True, null=True)  # Field name made lowercase.
    pvid = models.IntegerField(db_column='PVID', blank=True, null=True)  # Field name made lowercase.
    crossbow_id = models.IntegerField(db_column='CROSSBOW_ID', blank=True, null=True)  # Field name made lowercase.
    pv_name = models.CharField(db_column='PV_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='AREA', max_length=20, blank=True, null=True)  # Field name made lowercase.
    sca_code = models.CharField(db_column='SCA_CODE', max_length=7, blank=True, null=True)  # Field name made lowercase.
    power = models.FloatField(db_column='POWER', blank=True, null=True)  # Field name made lowercase.
    total_power = models.FloatField(db_column='TOTAL_POWER', blank=True, null=True)  # Field name made lowercase.
    pv_latitude = models.FloatField(db_column='PV_Latitude', blank=True, null=True)  # Field name made lowercase.
    pv_longitude = models.FloatField(db_column='PV_Longitude', blank=True, null=True)  # Field name made lowercase.
    module_model = models.IntegerField(blank=True, null=True)
    inverter_model = models.IntegerField(db_column='Inverter_model', blank=True, null=True)  # Field name made lowercase.
    array_tilt = models.FloatField(db_column='Array_Tilt', blank=True, null=True)  # Field name made lowercase.
    array_azimuth = models.FloatField(db_column='Array_Azimuth', blank=True, null=True)  # Field name made lowercase.
    array_stringinseries = models.IntegerField(db_column='Array_StringInSeries', blank=True, null=True)  # Field name made lowercase.
    array_stringinparallel = models.IntegerField(db_column='Array_StringInParallel', blank=True, null=True)  # Field name made lowercase.
    sandia_model_parama = models.FloatField(db_column='SANDIA_Model_ParamA', blank=True, null=True)  # Field name made lowercase.
    sandia_model_paramb = models.FloatField(db_column='SANDIA_Model_ParamB', blank=True, null=True)  # Field name made lowercase.
    albedo = models.FloatField(db_column='Albedo', blank=True, null=True)  # Field name made lowercase.
    pv_altitude = models.FloatField(db_column='PV_Altitude', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimPVCluster'


class Dimpvinverter(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100)  # Field name made lowercase.
    vac = models.IntegerField(db_column='Vac')  # Field name made lowercase.
    pac0 = models.FloatField(db_column='Pac0')  # Field name made lowercase.
    pdc0 = models.FloatField(db_column='Pdc0')  # Field name made lowercase.
    vdc0 = models.FloatField(db_column='Vdc0')  # Field name made lowercase.
    ps0 = models.FloatField(db_column='Ps0')  # Field name made lowercase.
    c0 = models.FloatField(db_column='C0')  # Field name made lowercase.
    c1 = models.FloatField(db_column='C1')  # Field name made lowercase.
    c2 = models.FloatField(db_column='C2')  # Field name made lowercase.
    c3 = models.FloatField(db_column='C3')  # Field name made lowercase.
    pnt = models.FloatField(db_column='Pnt')  # Field name made lowercase.
    vdcmax = models.FloatField(db_column='Vdcmax')  # Field name made lowercase.
    idcmax = models.FloatField(db_column='Idcmax')  # Field name made lowercase.
    mpptlow = models.IntegerField(db_column='MPPTLow')  # Field name made lowercase.
    mppthi = models.IntegerField(db_column='MPPTHi')  # Field name made lowercase.
    librarytype = models.CharField(db_column='LibraryType', max_length=50)  # Field name made lowercase.
    libraryname = models.CharField(db_column='LibraryName', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimPVInverter'


class Dimpvmodule(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    vintage = models.CharField(db_column='Vintage', max_length=50)  # Field name made lowercase.
    module_area_m_2_field = models.FloatField(db_column='Module_Area__m_2_')  # Field name made lowercase. Field renamed because it contained more than one '_' in a row. Field renamed because it ended with '_'.
    material = models.CharField(db_column='Material', max_length=50)  # Field name made lowercase.
    series_cells = models.IntegerField(db_column='Series_Cells')  # Field name made lowercase.
    parallel_c_s = models.IntegerField(db_column='Parallel_C_S')  # Field name made lowercase.
    isco = models.FloatField(db_column='Isco')  # Field name made lowercase.
    voco = models.FloatField(db_column='Voco')  # Field name made lowercase.
    impo = models.FloatField(db_column='Impo')  # Field name made lowercase.
    vmpo = models.FloatField(db_column='Vmpo')  # Field name made lowercase.
    aisc = models.FloatField(db_column='aIsc')  # Field name made lowercase.
    aimp = models.FloatField(db_column='aImp')  # Field name made lowercase.
    c0 = models.FloatField(db_column='C0')  # Field name made lowercase.
    c1 = models.FloatField(db_column='C1')  # Field name made lowercase.
    bvoco = models.FloatField(db_column='BVoco')  # Field name made lowercase.
    mbvoc = models.IntegerField(db_column='mBVoc')  # Field name made lowercase.
    bvmpo = models.FloatField(db_column='BVmpo')  # Field name made lowercase.
    mbvmp = models.IntegerField(db_column='mBVmp')  # Field name made lowercase.
    n = models.FloatField()
    c2 = models.FloatField(db_column='C2')  # Field name made lowercase.
    c3 = models.FloatField(db_column='C3')  # Field name made lowercase.
    a0 = models.FloatField(db_column='A0')  # Field name made lowercase.
    a1 = models.FloatField(db_column='A1')  # Field name made lowercase.
    a2 = models.FloatField(db_column='A2')  # Field name made lowercase.
    a3 = models.FloatField(db_column='A3')  # Field name made lowercase.
    a4 = models.FloatField(db_column='A4')  # Field name made lowercase.
    b0 = models.IntegerField(db_column='B0')  # Field name made lowercase.
    b1 = models.FloatField(db_column='B1')  # Field name made lowercase.
    b2 = models.FloatField(db_column='B2')  # Field name made lowercase.
    b3 = models.FloatField(db_column='B3')  # Field name made lowercase.
    b4 = models.FloatField(db_column='B4')  # Field name made lowercase.
    b5 = models.FloatField(db_column='B5')  # Field name made lowercase.
    d_tc_field = models.IntegerField(db_column='d_Tc_')  # Field name made lowercase. Field renamed because it ended with '_'.
    fd = models.IntegerField()
    a = models.FloatField()
    b = models.FloatField()
    c4 = models.FloatField(db_column='C4')  # Field name made lowercase.
    c5 = models.FloatField(db_column='C5')  # Field name made lowercase.
    ixo = models.FloatField(db_column='Ixo')  # Field name made lowercase.
    ixxo = models.FloatField(db_column='Ixxo')  # Field name made lowercase.
    c6 = models.FloatField(db_column='C6')  # Field name made lowercase.
    c7 = models.FloatField(db_column='C7')  # Field name made lowercase.
    data_source = models.IntegerField(db_column='Data_source', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimPVModule'


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
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Model_Name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    desc = models.TextField(db_column='Desc', blank=True, null=True)  # Field name made lowercase.
    productiontypeemieid = models.IntegerField(db_column='ProductionTypeEmieID', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DimRESGenForecastModel'


class Dimresgenforecastservice(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    Service_Name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    resid = models.IntegerField(db_column='RESID', blank=True, null=True)  # Field name made lowercase.
    reslevel = models.CharField(db_column='RESLevel', max_length=45, blank=True, null=True)  # Field name made lowercase.
    productiontypeemieid = models.IntegerField(db_column='ProductionTypeEmieID', blank=True, null=True)  # Field name made lowercase.
    marketsegment = models.TextField(db_column='MarketSegment', blank=True, null=True)  # Field name made lowercase.
    modelid = models.TextField(db_column='ModelID', blank=True, null=True)  # Field name made lowercase.
    horizon = models.IntegerField(db_column='Horizon', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DimRESGenForecastService'

"""
class Dimresunit(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    resunitname = models.TextField(db_column='RESUnitName', blank=True, null=True)  # Field name made lowercase.
    resunittype = models.TextField(db_column='RESUnitType', blank=True, null=True)  # Field name made lowercase.
    resunitarea = models.TextField(db_column='RESUnitArea', blank=True, null=True)  # Field name made lowercase.
    pstid = models.IntegerField(db_column='PStID', blank=True, null=True)  # Field name made lowercase.
    busid = models.IntegerField(db_column='BusID', blank=True, null=True)  # Field name made lowercase.
    totalpower = models.FloatField(db_column='TotalPower', blank=True, null=True)  # Field name made lowercase.
    losszone = models.BigIntegerField(db_column='LossZone', blank=True, null=True)  # Field name made lowercase.
    biddingzone = models.BigIntegerField(db_column='BiddingZone', blank=True, null=True)  # Field name made lowercase.
    participant = models.BigIntegerField(db_column='Participant', blank=True, null=True)  # Field name made lowercase.
    resuniteic = models.BigIntegerField(db_column='RESUnitEIC', blank=True, null=True)  # Field name made lowercase.
    locationid = models.IntegerField(db_column='LocationID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimRESUnit'


class Dimresunitref(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    arearefname = models.TextField(db_column='AreaRefName', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    zone = models.TextField(db_column='Zone', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimRESUnitRef'


class Dimwindturbinebrand(models.Model):
    wtbrandid = models.IntegerField(db_column='WTBrandID', primary_key=True)  # Field name made lowercase.
    wtbrandname = models.CharField(db_column='WTBrandName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    wt_nominalpower = models.FloatField(db_column='WT_NominalPower', blank=True, null=True)  # Field name made lowercase.
    wt_activepower = models.IntegerField(db_column='WT_ActivePower', blank=True, null=True)  # Field name made lowercase.
    wt_speedcutin = models.IntegerField(db_column='WT_SpeedCutIn', blank=True, null=True)  # Field name made lowercase.
    wt_speedrated = models.IntegerField(db_column='WT_SpeedRated', blank=True, null=True)  # Field name made lowercase.
    wt_speedcutoff = models.IntegerField(db_column='WT_SpeedCutOff', blank=True, null=True)  # Field name made lowercase.
    wt_hubheight = models.IntegerField(db_column='WT_HubHeight', blank=True, null=True)  # Field name made lowercase.
    wt_rotordiameter = models.IntegerField(db_column='WT_RotorDiameter', blank=True, null=True)  # Field name made lowercase.
    wt_curvespeed = models.FloatField(db_column='WT_CurveSpeed', blank=True, null=True)  # Field name made lowercase.
    wt_curvepower = models.FloatField(db_column='WT_CurvePower', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimWindTurbineBrand'


class Dimwindturbinecluster(models.Model):
    wfid = models.IntegerField(db_column='WFID', blank=True, null=True)  # Field name made lowercase.
    crossbow_id = models.IntegerField(db_column='CROSSBOW_ID', blank=True, null=True)  # Field name made lowercase.
    wf_name = models.TextField(db_column='WF_Name', blank=True, null=True)  # Field name made lowercase.
    wf_site_name = models.TextField(db_column='WF_site_name', blank=True, null=True)  # Field name made lowercase.
    powerstationid = models.TextField(db_column='PowerStationId', blank=True, null=True)  # Field name made lowercase.
    busid = models.IntegerField(db_column='Busid', blank=True, null=True)  # Field name made lowercase.
    traincode = models.IntegerField(db_column='TrainCode', blank=True, null=True)  # Field name made lowercase.
    displaycode = models.TextField(db_column='DisplayCode', blank=True, null=True)  # Field name made lowercase.
    totalpower = models.FloatField(db_column='TotalPower', blank=True, null=True)  # Field name made lowercase.
    sca_code = models.TextField(db_column='SCA_CODE', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(db_column='Lat', blank=True, null=True)  # Field name made lowercase.
    lon = models.FloatField(db_column='Lon', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DimWindTurbineCluster'


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
    create_service = models.BigIntegerField(blank=True, null=True)
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
