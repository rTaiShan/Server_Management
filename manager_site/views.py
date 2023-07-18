from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .actions.index import get_context_index

def index(request):
    template = loader.get_template("manager_site/index.html")
    context = get_context_index()
    return HttpResponse(template.render(context, request))
