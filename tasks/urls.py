from rest_framework.routers import DefaultRouter
from tasks import viewsets

router = DefaultRouter()
router.register(r'grupos', viewsets.GrupoViewSet)
router.register(r'etiquetas', viewsets.EtiquetaViewSet)
router.register(r'tarefas', viewsets.TarefaViewSet)

urlpatterns = router.urls
