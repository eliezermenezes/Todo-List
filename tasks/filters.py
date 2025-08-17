from django_filters import filterset
from tasks import models


class TarefaFilter(filterset.FilterSet):
    class Meta:
        model = models.Tarefa
        fields = ('nome', 'concluida', 'grupo')
