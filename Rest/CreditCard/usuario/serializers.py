from rest_framework import serializers
from .models import TipoUsuario, Usuario

class TipoUsuarioSerializer(serializers.Serializer):

    id = serializers.IntegerField(source='id_tipo_usuario', read_only=True)
    tipo_usuario = serializers.CharField(max_length=20)
    nivel = serializers.IntegerField(min_value=1, max_value=5)

    def create(self, validated_data):
        return TipoUsuario.objects.create(**validated_data)

class UsuarioSerializer(serializers.Serializer):

    id = serializers.IntegerField(source='id_usuario', read_only=True)
    # id_tipo_usuario = models.ForeignKey(TipoUsuario, models.DO_NOTHING, db_column='id_tipo_usuario')
    # tipo_usuario = serializers.IntegerField(source='id_tipo_usuario')
    tipo_usuario = serializers.PrimaryKeyRelatedField(source='id_tipo_usuario', queryset=TipoUsuario.objects.all())
    # jefe_id_usuario = models.ForeignKey('self', models.DO_NOTHING, db_column='jefe_id_usuario')
    # jefe = serializers.IntegerField(source='jefe_id_usuario')
    jefe = serializers.PrimaryKeyRelatedField(source='jefe_id_usuario', queryset=Usuario.objects.all())
    nombre = serializers.CharField(source='us_nombre', max_length=30)
    apaterno = serializers.CharField(source='us_apat', max_length=30)
    amaterno = serializers.CharField(source='us_amat', max_length=30)
    celular = serializers.CharField(source='us_celular', max_length=30, allow_blank=True, allow_null=True, required=False)
    email = serializers.CharField(source='us_email', max_length=45, allow_blank=True, allow_null=True, required=False)
    user = serializers.CharField(source='us_user', max_length=15)
    password = serializers.CharField(source='us_pass', max_length=35)
    
    def create(self, validated_data):
        return Usuario.objects.create(**validated_data)
