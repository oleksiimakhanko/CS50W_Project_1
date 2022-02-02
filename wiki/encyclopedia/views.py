from django.http import HttpResponseRedirect, QueryDict, HttpResponse
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


def search(request):
    entries = util.list_entries()
    search_results = []
    search_box = request.GET.get("q", "")

    if not request.GET.get('q'):
        return render(request, "encyclopedia/search.html", {"no_result": "You submitted nothing"})

    elif search_box in entries:
        return HttpResponseRedirect(f"./{search_box}")
    else:
        for en in entries:
            if search_box.lower() in en.lower():
                search_results.insert(0, en)
        if len(search_results) != 0:
            return render(request, "encyclopedia/search.html", {"search_results": search_results})
        else:
            return render(request, "encyclopedia/search.html", {"no_result": f"No results for {search_box}"})
