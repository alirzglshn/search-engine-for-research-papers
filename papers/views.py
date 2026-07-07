from django.core.paginator import Paginator
from django.shortcuts import render

from papers.forms import SearchForm
from papers.services.paper_search_service import search_papers


def home(request):
    form = SearchForm()
    return render(request, "papers/home.html", {"form": form})


def search_results(request):
    form = SearchForm(request.GET or None)
    query = ""
    page_obj = None

    if form.is_valid():
        query = form.cleaned_data["q"]
        results = search_papers(query)
        paginator = Paginator(results, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

    context = {
        "form": form,
        "query": query,
        "page_obj": page_obj,
        # True when a search has been run (even if it returned 0 results).
        "searched": page_obj is not None,
    }
    return render(request, "papers/results.html", context)