from django.http import HttpResponse
from django.shortcuts import render
from training.models import Counter


def homePageView(request):
    c, created = Counter.objects.get_or_create(value=1, eee=1)
    c.value = c.value+1
    c.save()

    context={
        'Counter': c.value
    }
    return render(request, 'counter.html', context)