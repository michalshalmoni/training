from django.http import HttpResponse
from django.shortcuts import render
from training.models import Counter


def homePageView(request):
    counter = Counter.objects.get(id=3)


    context={
        'Counter': counter.value
    }
    return render(request, 'counter.html', context)