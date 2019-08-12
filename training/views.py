from django.http import HttpResponse
from django.shortcuts import render


def homePageView(request):
    context={
        'Counter': 1
    }
    return render(request, 'counter.html', context)