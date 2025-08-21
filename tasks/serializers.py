from rest_framework import serializers
from tasks import models


class GrupoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Grupo
        fields = '__all__'


class EtiquetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Etiqueta
        fields = '__all__'


class TarefaSerializer(serializers.ModelSerializer):
    grupo = GrupoSerializer(read_only=True)
    etiquetas = EtiquetaSerializer(many=True, read_only=True)

    grupo_id = serializers.PrimaryKeyRelatedField(
        source='grupo',
        queryset=models.Grupo.objects.all(),
        write_only=True
    )
    etiquetas_ids = serializers.PrimaryKeyRelatedField(
        source='etiquetas',
        queryset=models.Etiqueta.objects.all(),
        many=True,
        write_only=True
    )

    class Meta:
        model = models.Tarefa
        fields = '__all__'
