from rest_framework import serializers
from .models import Solicitud

from usuario.models import Usuario
from catalogo.models import Producto, Situacionagen, Lugarapertura, Localidad, Statusfinal, Universidad, Causarechazo

class SolicitudSerializer(serializers.Serializer):
    # id_solicitud = models.AutoField(primary_key=True)
    id = serializers.IntegerField(source='id_solicitud', read_only=True)
    # id_usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='id_usuario')
    usuario = serializers.PrimaryKeyRelatedField(source='id_usuario', queryset=Usuario.objects.all())
    # id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='id_producto')
    producto = serializers.PrimaryKeyRelatedField(source='id_producto', queryset=Producto.objects.all())
    # folio = models.CharField(unique=True, max_length=30)
    folio = serializers.CharField(max_length=30)
    # sol_nombre = models.CharField(max_length=30)
    nombre = serializers.CharField(source='sol_nombre', max_length=30)
    # sol_apat = models.CharField(max_length=30)
    apellidoP = serializers.CharField(source='sol_apat', max_length=30)
    # sol_amat = models.CharField(max_length=30)
    apellidoM = serializers.CharField(source='sol_amat', max_length=30)
    # lada = models.CharField(max_length=10, blank=True, null=True)
    lada = serializers.CharField(max_length=10, allow_blank=True, allow_null=True, required=False)
    # telefono = models.CharField(max_length=20, blank=True, null=True)
    telefono = serializers.CharField(max_length=20, allow_blank=True, allow_null=True, required=False)
    # email = models.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    # id_lugarapertura = models.ForeignKey(Lugarapertura, models.DO_NOTHING, db_column='id_lugarApertura')  # Field name made lowercase.
    apertura = serializers.PrimaryKeyRelatedField(source='id_lugarapertura', queryset=Lugarapertura.objects.all())
    # id_localidad = models.ForeignKey(Localidad, models.DO_NOTHING, db_column='id_localidad')
    localidad = serializers.PrimaryKeyRelatedField(source='id_localidad', queryset=Localidad.objects.all())
    # dictamen = models.CharField(max_length=16, blank=True, null=True)
    dictamen = serializers.CharField(max_length=16, allow_blank=True, allow_null=True, required=False)
    # semaforo = models.CharField(max_length=8, blank=True, null=True)
    semaforo = serializers.CharField(max_length=8, allow_blank=True, allow_null=True, required=False)
    # fechacaptura = models.DateField(db_column='fechaCaptura')  # Field name made lowercase.
    fechacaptura = serializers.DateField()
    # fechadecision = models.DateField(db_column='fechaDecision')  # Field name made lowercase.
    fechadecision = serializers.DateField(required=False)
    # id_situacionagen = models.ForeignKey(Situacionagen, models.DO_NOTHING, db_column='id_situacionAgen')  # Field name made lowercase.
    situacionagen = serializers.PrimaryKeyRelatedField(source='id_situacionagen', queryset=Situacionagen.objects.all())
    # situacionsol = models.CharField(db_column='situacionSol', max_length=18, blank=True, null=True)  # Field name made lowercase.
    situacionsol = serializers.CharField(max_length=18, allow_blank=True, allow_null=True, required=False)
    # id_statusfinal = models.ForeignKey('Statusfinal', models.DO_NOTHING, db_column='id_statusFinal')  # Field name made lowercase.
    statusfinal = serializers.PrimaryKeyRelatedField(source='id_statusfinal', queryset=Statusfinal.objects.all())
    # id_causarechazo = models.ForeignKey(Causarechazo, models.DO_NOTHING, db_column='id_causaRechazo', blank=True, null=True)  # Field name made lowercase.
    causarechazo = serializers.PrimaryKeyRelatedField(source='id_causarechazo', queryset=Causarechazo.objects.all())
    # fechacarga = models.DateField(db_column='fechaCarga')  # Field name made lowercase.
    fechacarga = serializers.DateField(required=False)
    # fechavigencia = models.DateField(db_column='fechaVigencia')  # Field name made lowercase.
    fechavigencia = serializers.DateField(required=False)
    # cuestionario = models.CharField(max_length=11)
    cuestionario = serializers.CharField(max_length=11, allow_blank=True, allow_null=True, required=False)
    # tokenefi = models.CharField(db_column='tokenEfi', max_length=20)  # Field name made lowercase.
    tokenefi = serializers.CharField(max_length=20, allow_blank=True, allow_null=True, required=False)
    # formalizada = models.CharField(max_length=2)
    formalizada = serializers.CharField(max_length=2, allow_blank=True, allow_null=True, required=False)
    # fechaformal = models.DateField(db_column='fechaFormal')  # Field name made lowercase.
    fechaformal = serializers.DateField(required=False)
    # codigocliente = models.CharField(db_column='codigoCliente', max_length=20)  # Field name made lowercase.
    codigocliente = serializers.CharField(max_length=20, allow_blank=True, allow_null=True)
    # puntoventa = models.CharField(db_column='puntoVenta', max_length=60, blank=True, null=True)  # Field name made lowercase.
    puntoventa = serializers.CharField(max_length=60, allow_blank=True, allow_null=True)
    # observacion = models.TextField(blank=True, null=True)
    observacion = serializers.CharField(allow_blank=True, allow_null=True, required=False)

class Zero(serializers.Serializer):
    # id_zero = models.IntegerField(primary_key=True)
    id = serializers.IntegerField(source='id_zero', read_only=True)
    # id_solicitud = models.ForeignKey(Solicitud, models.DO_NOTHING, db_column='id_solicitud')
    solicitud = serializers.PrimaryKeyRelatedField(source='id_solicitud', queryset=Solicitud.objects.all())
    # id_universidad = models.ForeignKey(Universidad, models.DO_NOTHING, db_column='id_universidad')
    universidad = serializers.PrimaryKeyRelatedField(source='id_universidad', queryset=Universidad.objects.all())
    # campus = models.CharField(max_length=45, blank=True, null=True)
    campus = serializers.CharField(max_length=45, allow_blank=True, allow_null=True, required=False)
    # carrera = models.CharField(max_length=45, blank=True, null=True)
    carrera = serializers.CharField(max_length=45, allow_blank=True, allow_null=True, required=False)
    # colegiatura = models.FloatField(blank=True, null=True)
    colegiatura = serializers.FloatField(allow_blank=True, allow_null=True, required=False)
    # financiamiento = models.CharField(max_length=11, blank=True, null=True)
    financiamiento = serializers.CharField(max_length=11, allow_blank=True, allow_null=True, required=False)
    # ingresofam = models.FloatField(db_column='ingresoFam', blank=True, null=True)  # Field name made lowercase.
    ingresofam = serializers.FloatField(allow_blank=True, allow_null=True, required=False)
    # procentajebeca = models.FloatField(db_column='procentajeBeca', blank=True, null=True)  # Field name made lowercase.
    procentajebeca = serializers.FloatField(allow_blank=True, allow_null=True, required=False)
    # gradoesc = models.CharField(db_column='gradoEsc', max_length=45, blank=True, null=True)  # Field name made lowercase.
    gradoesc = serializers.CharField(max_length=45, allow_blank=True, allow_null=True, required=False)


