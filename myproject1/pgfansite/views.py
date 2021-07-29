from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone

from .models import Thread,Response

def index(request):
    threads = Thread.objects.order_by('-updatedttm')
    return render(request, 'pgfansite/index.html', {'threads':threads})

def detail(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    responses = Response.objects.filter(thread=thread).order_by('resno')
    return render(request, 'pgfansite/detail.html', {'thread':thread,'responses':responses})

def thread(request):
    return render(request, 'pgfansite/thread.html')

def res_insert(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    new_response = Response(thread=thread, resno=thread.response_count+1 , username=request.POST['username'], body=request.POST['body'])
    new_response.save()
    thread.response_count += 1
    thread.updatedttm = new_response.published
    thread.save()
    return HttpResponseRedirect(reverse('pgfansite:detail', args=(thread.id,)))

def thread_insert(request):
    return render(request, 'pgfansite/thread.html')