from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Thread,Response

def index(request):
    threads = Thread.objects.order_by('-updatedttm')
    return render(request, 'pgfansite/index.html', {'threads':threads})

def detail(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    return render(request, 'pgfansite/detail.html', {'thread':thread})
