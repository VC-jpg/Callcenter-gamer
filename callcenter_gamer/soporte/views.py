from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Pregunta, Respuesta
from .forms import PreguntaForm, RespuestaForm

def landing_page(request):
    return render(request, 'soporte/landing.html')

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'soporte/registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'soporte/iniciar_sesion.html')

@login_required
def home(request):
    if request.user.is_staff:
        preguntas = Pregunta.objects.all()
    else:
        preguntas = Pregunta.objects.filter(usuario=request.user)
    return render(request, 'soporte/home.html', {'preguntas': preguntas})

@login_required
def hacer_pregunta(request):
    if request.method == 'POST':
        form = PreguntaForm(request.POST)
        if form.is_valid():
            pregunta = form.save(commit=False)
            pregunta.usuario = request.user
            pregunta.save()
            return redirect('home')
    else:
        form = PreguntaForm()
    return render(request, 'soporte/hacer_pregunta.html', {'form': form})

@login_required
def responder_pregunta(request, pregunta_id):
    pregunta = get_object_or_404(Pregunta, id=pregunta_id)
    if request.method == 'POST':
        form = RespuestaForm(request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.usuario = request.user
            respuesta.pregunta = pregunta
            respuesta.save()
            return redirect('home')
    else:
        form = RespuestaForm()
    return render(request, 'soporte/responder_pregunta.html', {'form': form, 'pregunta': pregunta})
