from django.db import models


class ModeloBase(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True)
    modificado_em = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True



class Grupo(ModeloBase):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'grupo'
        verbose_name = 'Grupo'
        verbose_name_plural = 'Grupos'


class Etiqueta(ModeloBase):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'etiqueta'
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Etiquetas'


class Tarefa(ModeloBase):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    concluida = models.BooleanField(default=False)
    ordem = models.IntegerField(default=0)
    data_vencimento = models.DateField(blank=True, null=True)
    grupo = models.ForeignKey(
        to=Grupo,
        on_delete=models.CASCADE,
        related_name='tarefas',
        blank=True,
        null=True,
        db_column='grupo_id'
    )
    etiquetas = models.ManyToManyField(
        to=Etiqueta,
        related_name='tarefas',
        blank=True,
        db_table='tarefa_etiqueta',
    )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'tarefa'
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['ordem']
