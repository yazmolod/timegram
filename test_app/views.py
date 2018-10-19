from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

from . import magic as magic_module

def index(request):
	t = loader.get_template('test.html')
	html = t.render({'current_date': datetime.now()})
	return HttpResponse(html)

def magic(request):
	if magic_module.ig.login():
		magic_module.DoMagic()
		return HttpResponse("Is something happend?")
	else:
		print ('fail')
		return HttpResponse(":((((((")