from rest_framework import serializers
from .models import TipoUsuario

class TipoUsuarioSerializer(serializers.Serializer):

    id = serializers.IntegerField(source='id_tipo_usuario', read_only=True)
    tipo_usuario = serializers.CharField(max_length=20)
    nivel = serializers.IntegerField(min_value=1, max_value=5)

    def create(self, validated_data):
        return TipoUsuario.object.create(**validated_data)
