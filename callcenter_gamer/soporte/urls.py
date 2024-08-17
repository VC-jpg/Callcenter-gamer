from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('registro/', views.registro, name='registro'),
    path('iniciar_sesion/', views.iniciar_sesion, name='iniciar_sesion'),
    path('home/', views.home, name='home'),
    path('preguntar/', views.hacer_pregunta, name='hacer_pregunta'),
    path('responder/<int:pregunta_id>/', views.responder_pregunta, name='responder_pregunta'),
]
