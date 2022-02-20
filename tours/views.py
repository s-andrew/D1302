from django.http import Http404
from django.shortcuts import render


def index_view(request):
    return render(request, "tours/index.html")


def departure_view(request, departure):
    return render(request, "tours/departure.html")


def tour_view(request, pk):
    raise Http404
    return render(request, "tours/tour.html")
