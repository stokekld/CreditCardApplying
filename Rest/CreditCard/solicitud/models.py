from __future__ import unicode_literals

from django.db import models

class Solicitud(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')
    folio = models.CharField(unique=True, max_length=30)
    sol_nombre = models.CharField(max_length=30)
    sol_apat = models.CharField(max_length=30)
    sol_amat = models.CharField(max_length=30)
    lada = models.CharField(max_length=10, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50)
    id_lugarapertura = models.ForeignKey(Lugarapertura, models.DO_NOTHING, db_column='id_lugarApertura')  # Field name made lowercase.
    id_localidad = models.ForeignKey(Localidad, models.DO_NOTHING, db_column='id_localidad')
    dictamen = models.CharField(max_length=16, blank=True, null=True)
    semaforo = models.CharField(max_length=8, blank=True, null=True)
    fechacaptura = models.DateField(db_column='fechaCaptura')  # Field name made lowercase.
    fechadecision = models.DateField(db_column='fechaDecision')  # Field name made lowercase.
    id_situacionagen = models.ForeignKey(Situacionagen, models.DO_NOTHING, db_column='id_situacionAgen')  # Field name made lowercase.
    situacionsol = models.CharField(db_column='situacionSol', max_length=18, blank=True, null=True)  # Field name made lowercase.
    id_statusfinal = models.ForeignKey('Statusfinal', models.DO_NOTHING, db_column='id_statusFinal')  # Field name made lowercase.
    id_causarechazo = models.ForeignKey(Causarechazo, models.DO_NOTHING, db_column='id_causaRechazo', blank=True, null=True)  # Field name made lowercase.
    fechacarga = models.DateField(db_column='fechaCarga')  # Field name made lowercase.
    fechavigencia = models.DateField(db_column='fechaVigencia')  # Field name made lowercase.
    cuestionario = models.CharField(max_length=11)
    tokenefi = models.CharField(db_column='tokenEfi', max_length=20)  # Field name made lowercase.
    formalizada = models.CharField(max_length=2)
    fechaformal = models.DateField(db_column='fechaFormal')  # Field name made lowercase.
    codigocliente = models.CharField(db_column='codigoCliente', max_length=20)  # Field name made lowercase.
    puntoventa = models.CharField(db_column='puntoVenta', max_length=60, blank=True, null=True)  # Field name made lowercase.
    observacion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'solicitud'

class Zero(models.Model):
    id_zero = models.IntegerField(primary_key=True)
    id_solicitud = models.ForeignKey(Solicitud, models.DO_NOTHING, db_column='id_solicitud')
    id_universidad = models.ForeignKey(Universidad, models.DO_NOTHING, db_column='id_universidad')
    universidad = models.CharField(max_length=45, blank=True, null=True)
    campus = models.CharField(max_length=45, blank=True, null=True)
    carrera = models.CharField(max_length=45, blank=True, null=True)
    colegiatura = models.FloatField(blank=True, null=True)
    financiamiento = models.CharField(max_length=11, blank=True, null=True)
    ingresofam = models.FloatField(db_column='ingresoFam', blank=True, null=True)  # Field name made lowercase.
    procentajebeca = models.FloatField(db_column='procentajeBeca', blank=True, null=True)  # Field name made lowercase.
    gradoesc = models.CharField(db_column='gradoEsc', max_length=45, blank=True, null=True)  # Field name made lowercase.

class Meta:
    managed = False
    db_table = 'zero'

