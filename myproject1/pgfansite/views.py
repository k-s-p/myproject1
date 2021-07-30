from django.http.response import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.template import loader

from .models import Thread,Response
from .forms import PhotoForm

def index(request):
    threads = Thread.objects.order_by('-updatedttm')
    return render(request, 'pgfansite/index.html', {'threads':threads})

def detail(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    responses = Response.objects.filter(thread=thread).order_by('resno')
    return render(request, 'pgfansite/detail.html', {'thread':thread,'responses':responses})

def thread(request):
    template = loader.get_template('pgfansite/thread.html')
    context = {'form':PhotoForm()}
    return HttpResponse(template.render(context, request))

def res_insert(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    new_response = Response(thread=thread, resno=thread.response_count+1 , username=request.POST['username'], body=request.POST['body'])
    new_response.save()
    thread.response_count += 1
    thread.updatedttm = new_response.published
    thread.save()
    return HttpResponseRedirect(reverse('pgfansite:detail', args=(thread.id,)))

def newthread(request):
    if request.method == 'POST':
        new_thread = Thread()
        new_thread.title = request.POST['title']
        if 'image' in request.FILES:
            new_thread.image = request.FILES['image']
        new_thread.username = request.POST['username']
        new_thread.body = request.POST['body']
        new_thread.save()
        return render(request, 'pgfansite/detail.html', {'thread':new_thread})
    else:
        #URL直接入力された際の回避
        #もっと実用的な方法があるなら知りたい、、、
        threads = Thread.objects.order_by('-updatedttm')
        return render(request, 'pgfansite/index.html', {'threads':threads})