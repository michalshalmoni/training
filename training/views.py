from django.http import HttpResponse
from django.shortcuts import render
from training.models import Counter


def homePageView(request):
    counter = 3#Counter.objects.get(id=3)
    # counter.value = counter.value+1
    # counter.save()



    context={
        'Counter': counter.value
    }
    return render(request, 'counter.html', context)