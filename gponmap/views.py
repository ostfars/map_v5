from django.shortcuts import render
from django.views.generic.base import TemplateView


class GponmapView(TemplateView):
    template_name = "map.html"
