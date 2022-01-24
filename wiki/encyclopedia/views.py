from django.http import HttpResponse
from django.shortcuts import render

import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def new(request):
    return render(request, "encyclopedia/new_entry.html")


def entry(request, name):
    return render(request, "encyclopedia/entry.html", {
        "content": markdown2.markdown(util.get_entry(name))
    })
