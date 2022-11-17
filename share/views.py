from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .models import *
from .forms import *


def index(request):
    context = {}

    return render(request, 'index.html', context)


class SalvarVideo(CreateView):
    model = Video
    form_class = NovoVideoForm
    template_name = 'novo_video_form.html'
    success_url = reverse_lazy('lista_video')


def lista_videos(request):
    context = {}
    usuario_id = request.user.id

    videos_pub = Video.objects.filter(publico=True)
    videos_priv = Video.objects.filter(publico=False, usuarios__id=usuario_id)
    context['videos_pub'] = videos_pub
    context['videos_priv'] = videos_priv

    return render(request, 'lista_videos.html', context)


def exibe_video(request, video_id):
    context = {}

    video = Video.objects.get(id=video_id)
    video.views += 1
    video.save()
    link = video.link
    if 'v=' in link:
        link = link.split('v=')[1]
        if '&' in link:
            link = link.split('&')[0]
        link = 'https://www.youtube.com/embed/' + link

    if 'youtu.be' in link:
        link = link.split('/')[-1]
        link = 'https://www.youtube.com/embed/' + link

    context['url_video'] = link
    context['views'] = video.views
    context['video_id'] = video_id

    return render(request, 'visualiza_video.html', context)


def exibe_comentarios(request, video_id):
    context = {}

    comentarios = Comentario.objects.filter(video__id=video_id)
    context['comentarios'] = comentarios
    context['video_id'] = video_id

    return render(request, 'comentarios.html', context)


def salva_comentario(request):
    if request.method == "POST":
        usuario_id = request.POST['usuario']
        usuario = User.objects.get(id=usuario_id)
        comentario = request.POST['comentario']
        video_id = request.POST['video_id']
        video = Video.objects.get(id=video_id)

        novo_comentario = Comentario(usuario=usuario, video=video, comentario=comentario)
        novo_comentario.save()

        return redirect('exibe_comentarios', video_id)


def signup(request):
    context = {}
    return render(request, 'signup.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username, email, password)
        user.save()

        return redirect('index')


def login_request(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:  # verificando se usuario esta bloqueado
                login(request, user)
                return redirect('index')
        else:
            context['message'] = "Usuário ou senha inválido."
            return render(request, 'error.html', context)


def logout_request(request):
    logout(request)
    return redirect('index')
