from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView
from django.views.generic import DetailView


class Pagar(DetailView):
    def get(self, *args, **kwargs):
        return HttpResponse('Pagar')


class SalvarPedido(View):
    def get(self, *args, **kwargs):
        return HttpResponse('SalvarPedido')


class Lista(ListView):
    def get(self, *args, **kwargs):
        return HttpResponse('Lista')


class Detalhe(DetailView):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe')
