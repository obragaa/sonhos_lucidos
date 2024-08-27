from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SonhoViewSet
from . import views

router = DefaultRouter()
router.register(r'sonhos', SonhoViewSet)  # O prefixo 'sonhos' será usado para as rotas da API

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('api/', include(router.urls)),  # API REST acessível via /api/sonhos/
]