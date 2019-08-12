from django.http import HttpResponse
from django.shortcuts import render
from training.models import Counter


def homePageView(request):
    value = Counter.objects.get(id=3).values_list('value')


    context={
        'Counter': value
    }
    return render(request, 'counter.html', context)