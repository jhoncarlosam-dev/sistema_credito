from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario, Credito, Pago, Garantia
from .forms import UsuarioForm, CreditoForm, PagoForm, GarantiaForm

def listar_usuarios(request):
  usuarios = Usuario.objects.all()
  return render(request, 'credito/listar_usuarios.html', {'usuarios': usuarios})

def crear_usuarios(request):
  if request.method == 'POST':
    form = UsuarioForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('listar_usuarios')
  else:
    form = UsuarioForm()
  return render(request, 'credito/crear_usuario.html', {'form': form})

def editar_usuario(request, usuario_id):
  usuario = get_object_or_404(Usuario, id=usuario_id)
  if request.method == 'POST':
    form = UsuarioForm(request.POST, instance=usuario)
    if form.is_valid():
      form.save()
      return redirect('listar_usuarios')
  else:
    form = UsuarioForm(instance=usuario)
  return render(request, 'credito/editar_usuario.html', {'form': form})

def eliminar_usuario(request, usuario_id):
  usuario = get_object_or_404(Usuario, id=usuario_id)
  usuario.delete()
  return redirect('listar_usuarios')