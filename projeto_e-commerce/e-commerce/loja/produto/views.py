from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib import messages

from . import models


class ListaProdutos(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Listar')


class DetalheProduto(DetailView):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')


class AdicionarAoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar ao carrinho')


class RemoverDoCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover carrinho')


class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')


class ResumoDaCompra(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')
