from rest_framework import viewsets
from tasks import models, serializers, filters


class GrupoViewSet(viewsets.ModelViewSet):
    queryset = models.Grupo.objects.all()
    serializer_class = serializers.GrupoSerializer


class EtiquetaViewSet(viewsets.ModelViewSet):
    queryset = models.Etiqueta.objects.all()
    serializer_class = serializers.EtiquetaSerializer


class TarefaViewSet(viewsets.ModelViewSet):
    queryset = models.Tarefa.objects.all()
    serializer_class = serializers.TarefaSerializer
    filterset_class = filters.TarefaFilter
