# contrib packages
from django.contrib import messages

# class-based views
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView


class IndexView(TemplateView):
    template_name = 'index.html'
