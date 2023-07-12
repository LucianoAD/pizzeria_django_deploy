from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.http import JsonResponse

from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.views.generic.detail import DetailView


from .models import Pizza

class PizzasBaseView(View):
    template_name = 'pizzas.html'
    model = Pizza
    fields = '__all__'
    success_url = reverse_lazy('pizzas:all')


class PizzasListView(PizzasBaseView,ListView):
    """
    ESTO ME PERMITE CREAR UNA VISTA CON LAS PIZZAS
    """

class PizzasDetailView(PizzasBaseView,DetailView):
    template_name = "pizza_detail.html"

class PizzasCreateView(PizzasBaseView,CreateView):
    template_name = "pizza_create.html"
    extra_context = {
        "tipo": "Crear pizza"
    }


class PizzasUpdateView(PizzasBaseView,UpdateView):
    template_name = "pizza_create.html"
    extra_context = {
        "tipo": "Actualizar pizza"
    }

class PizzasDeleteView(PizzasBaseView,DeleteView):
    template_name = "pizza_delete.html"
    extra_context = {
        "tipo": "Borrar pizza"
    }

def get_pizzas_json(request):
    pizzas = Pizza.objects.all()
    pizzas_data = [{'nombre': pizza.nombre, 'descripcion': pizza.descripcion, 'ruta': pizza.imagen.url} for pizza in pizzas]
    return JsonResponse({'pizza': pizzas_data})