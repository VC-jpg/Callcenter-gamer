from django.contrib import admin
from .models import Pregunta, Respuesta

class PreguntaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'contenido', 'usuario')  # Asegúrate de que estos campos existan en el modelo
    list_filter = ('usuario',)  # Asegúrate de que estos campos existan en el modelo

class RespuestaAdmin(admin.ModelAdmin):
    list_display = ('contenido', 'pregunta', 'usuario', 'administrador')  # Asegúrate de que estos campos existan en el modelo
    list_filter = ('pregunta', 'usuario', 'administrador')  # Asegúrate de que estos campos existan en el modelo

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta, RespuestaAdmin)
