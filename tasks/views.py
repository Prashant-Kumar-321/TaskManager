from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect 

# Create your views here.

def index(request): 
	return HttpResponse("Hello Task Manager Web application") 
	# return the index.html tempalte 
	pass 