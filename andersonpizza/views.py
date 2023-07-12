from django.shortcuts import render
from django.views.generic import TemplateView

class andersonpizzaLandingClassView(TemplateView):
    template_name = 'landing_page.html'
    extra_context = {
        'base_on': 'Class Based View',
        'titulo_pagina': 'LANDING PAGE'
    }