from django.http import HttpResponse
from django.shortcuts import render


def homePageView(request):
    return render(request, 'training/templates/counter.html')