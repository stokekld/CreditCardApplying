from __future__ import unicode_literals

from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    producto = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'producto'

class Situacionagen(models.Model):
    id_situacionagen = models.AutoField(db_column='id_situacionAgen', primary_key=True)  # Field name made lowercase.
    situacionagen = models.CharField(db_column='situacionAgen', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'situacionAgen'

class Lugarapertura(models.Model):
    id_lugarapertura = models.AutoField(db_column='id_lugarApertura', primary_key=True)  # Field name made lowercase.
    lugarapertura = models.CharField(db_column='lugarApertura', max_length=80)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lugarApertura'

class Localidad(models.Model):
    id_localidad = models.AutoField(primary_key=True)
    localidad = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'localidad'

class Statusfinal(models.Model):
    id_statusfinal = models.AutoField(db_column='id_statusFinal', primary_key=True)  # Field name made lowercase.
    statusfinal = models.CharField(db_column='statusFinal', max_length=30)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'statusFinal'

class Universidad(models.Model):
    id_universidad = models.IntegerField(primary_key=True)
    universidad = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'universidad'

class Causarechazo(models.Model):
    id_causarechazo = models.AutoField(db_column='id_causaRechazo', primary_key=True)  # Field name made lowercase.
    causarechazo = models.CharField(db_column='causaRechazo', max_length=70)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'causaRechazo'
