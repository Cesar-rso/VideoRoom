from django.urls import path
from views import *


urlpatterns = [
    path('', index, name='index'),
    path('novo_video', SalvarVideo.as_view(), name='novo_video'),
    path('lista', lista_videos, name='lista_videos'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    path('signup', signup, name='signup'),
    path('register', register, name='register'),
]
