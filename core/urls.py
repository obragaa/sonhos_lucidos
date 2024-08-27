from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SonhoViewSet, CustomLoginView, RegisterView
from . import views
from django.contrib.auth.decorators import login_required

router = DefaultRouter()
router.register(r'sonhos', SonhoViewSet)  # O prefixo 'sonhos' será usado para as rotas da API

urlpatterns = [
    path('', login_required(views.index), name='index'),  # Protegendo a página inicial
    path('editar/<int:pk>/', views.editar_sonho, name='editar_sonho'),  # Rota para edição
    path('excluir/<int:pk>/', views.excluir_sonho, name='excluir_sonho'),  # Rota para exclusão
    path('login/', CustomLoginView.as_view(), name='login'),  # Rota para a página de login
    path('register/', RegisterView.as_view(), name='register'),  # Rota para a página de registro
    path('api/', include(router.urls)),  # API REST acessível via /api/sonhos/
]