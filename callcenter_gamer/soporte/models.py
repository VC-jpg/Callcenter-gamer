from django.db import models
from django.contrib.auth.models import User

class Pregunta(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='preguntas')
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Si necesitas este campo

class Respuesta(models.Model):
    contenido = models.TextField()
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respuestas')
    administrador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='respuestas_administrador')
    fecha_creacion = models.DateTimeField(auto_now_add=True)  # Si necesitas este campo
