from django.http import HttpResponse
from django.shortcuts import render
from training.models import Counter


def homePageView(request):
    c = Counter.objects.get(id=1)
    c.value = c.value+1
    c.save()

    context = {
        'Counter': c.value
    }
    return render(request, 'counter.html', context)