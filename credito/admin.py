from django.contrib import admin
from .models import Usuario, Credito, Pago, Garantia

admin.site.register(Usuario)
admin.site.register(Credito)
admin.site.register(Pago)
admin.site.register(Garantia)
