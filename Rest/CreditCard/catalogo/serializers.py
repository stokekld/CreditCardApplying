from rest_framework import serializers
from .models import Producto, Situacionagen, Lugarapertura, Localidad, Statusfinal, Universidad, Causarechazo

class ProductoSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='id_producto', read_only=True)
    producto = serializers.CharField(max_length=40)

class SituacionagenSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='id_situacionagen', read_only=True)
    situacionagen = serializers.CharField(max_length=60)

class LugaraperturaSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='id_lugarApertura', read_only=True)
    lugarapertura = serializers.CharField(max_length=80)

class LocalidadSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='id_localidad', read_only=True)
    localidad = serializers.CharField(max_length=80)

class StatusfinalSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='id_statusfinal', read_only=True)
    statusfinal = serializers.CharField(max_length=30)

class UniversidadSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='id_universidad', read_only=True)
    universidad = serializers.CharField(max_length=100)

class CausarechazoSerializer(serializers.Serializer):
    id = serializers.IntegerField(source='id_causarechazo', read_only=True)
    causarechazo = serializers.CharField(max_length=100)
