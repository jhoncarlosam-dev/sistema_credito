from django import forms
from .models import Usuario, Credito, Pago, Garantia

class UsuarioForm(forms.ModelForm):
  class Meta:
    model = Usuario
    fields = ['nombre', 'documento', 'correo', 'telefono', 'direccion']
    widget = {
      'direccion': forms.Textarea(attrs={'rows': 3}),
    }

class CreditoForm(forms.ModelForm):
  class Meta:
    model = Credito
    fields = ['usuario', 'monto', 'tasa_interes', 'plazo_meses', 'estado', 'fecha_inicio', 'fecha_fin']

class PagoForm(forms.ModelForm):
  class Meta:
    model = Pago
    fields = ['credito', 'monto', 'fecha_pago', 'metodo_pago']

class GarantiaForm(forms.ModelForm):
  class Meta:
    model = Garantia
    fields = ['credito', 'tipo_garantia', 'valor_estimado']