from django.db import models

class Usuario(models.Model):
  nombre = models.CharField(max_length=100)
  documento = models.CharField(max_length=20, unique=True)
  correo = models.EmailField(null=True, blank=True)
  telefono = models.CharField(max_length=15, null=True, blank=True)
  direccion = models.TextField(null=True, blank=True)
  fecha_registro = models.DateField(auto_now_add=True)

  def __str__(self):
    return self.nombre
  
class Credito(models.Model):
  ESTADO_CHOICES = [
    ('Activo', 'Activo'),
    ('Pagado', 'Pagado'),
    ('En mora', 'En mora')
  ]

  usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
  monto = models.DecimalField(max_digits=10, decimal_places=2)
  tasa_interes = models.DecimalField(max_digits=5, decimal_places=2)
  plazo_meses = models.PositiveIntegerField()
  estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default="Activo")
  fecha_inicio = models.DateField()
  fecha_fin = models.DateField(null=True, blank=True)

  def __str__(self):
    return f"Crédito {self.id} - {self.usuario.nombre}"
  
class Pago(models.Model):
  METODO_CHOICES = [
    ('Transferencia', 'Transferencia'),
    ('Efectivo', 'Efectivo'),
    ('Tarjeta', 'Tarjeta'),
  ]

  credito = models.ForeignKey(Credito, on_delete=models.CASCADE)
  monto = models.DecimalField(max_digits=10, decimal_places=2)
  fecha_pago = models.DateField()
  metodo_pago = models.CharField(max_length=20, choices=METODO_CHOICES)

  def __str__(self):
    return f"Pago {self.id} - Crédito {self.credito.id}"
  
class Garantia(models.Model):
  credito = models.ForeignKey(Credito, on_delete=models.CASCADE)
  tipo_garantia = models.CharField(max_length=50)
  valor_estimado = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return f"Garantía {self.id} - Crédito {self.credito.id}"
