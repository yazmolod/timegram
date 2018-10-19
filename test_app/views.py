from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

from .forms import ImageForm

from . import magic as magic_module


def index(request):
    form = ImageForm()
    t = loader.get_template('test.html')
    html = t.render({'current_date': datetime.now(), 'form': form})
    return HttpResponse(html)


def magic(request):
    caption = request.POST['image_caption']
    print('\n\n\n')
    print(request.FILES)
    print('\n\n\n')
    file = request.FILES['image_file']
    print(file)
    with open('tmp.jpg', 'wb+') as tmp:
        for chunk in file.chunks():
            tmp.write(chunk)
    if magic_module.ig.login():
        magic_module.DoMagic(caption)
        return HttpResponse("Is something happend?")
    else:
        magic_module.ig.logout()
        if magic_module.ig.login():
            magic_module.DoMagic(caption)
            return HttpResponse("Is something happend?")
        else:
            print('fail')
            return HttpResponse(":((((((")
