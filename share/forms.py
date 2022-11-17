from django import forms
from django.contrib.auth.models import User
from .models import *


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return member.name


class NovoVideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['titulo', 'descricao', 'link', 'usuarios', 'publico']

    titulo = forms.CharField(help_text='Coloque aqui o título do video')
    descricao = forms.CharField(help_text='Descreva brevemente o video')
    link = forms.CharField(help_text='Coloque aqui o link do video no Youtube')
    usuarios = CustomMMCF(widget=forms.CheckboxSelectMultiple, queryset=User.objects.all(),
                          help_text='Em caso de videos privado, escolha quais usuários terão acesso ao video')
    publico = forms.BooleanField(help_text='Defina se o video é público ou privado')
