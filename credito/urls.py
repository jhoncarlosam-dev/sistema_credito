from django.urls import path
from . import views

urlpatterns = [
  path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
  path('usuarios/crear/', views.crear_usuarios, name='crear_usuarios'),
  path('usuarios/editar/<int:usuario_id>/', views.editar_usuario, name='editar_usuario'),
  path('usuarios/eliminar/<int:usuario_id>/', views.eliminar_usuario, name='eliminar_usuario'),
]