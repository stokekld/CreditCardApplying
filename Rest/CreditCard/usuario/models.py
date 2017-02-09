from __future__ import unicode_literals

from django.db import models


class TipoUsuario(models.Model):
    id_tipo_usuario = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(max_length=20)
    nivel = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_usuario'

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    id_tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tipo_usuario')
    jefe_id_usuario = models.ForeignKey('self', models.DO_NOTHING, db_column='jefe_id_usuario')
    us_nombre = models.CharField(max_length=30)
    us_apat = models.CharField(max_length=30)
    us_amat = models.CharField(max_length=30)
    us_celular = models.CharField(max_length=30, blank=True, null=True)
    us_email = models.CharField(max_length=45, blank=True, null=True)
    us_user = models.CharField(unique=True, max_length=15)
    us_pass = models.CharField(max_length=35)

    class Meta:
        managed = False
        db_table = 'usuario'


