from django.urls import path
from views import *


urlpatterns = [
    path('', index, name='index'),
    path('login', login_request, name='login'),
    path('logout', logout_request, name='logout'),
    path('signup', signup, name='signup'),
    path('register', register, name='register'),
]
