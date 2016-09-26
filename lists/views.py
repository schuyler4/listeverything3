from django.shortcuts import render
from django.http import HttpResponse
from .models import List, List_Item

# Create your views here.
def index(request):
	return HttpResponse("hello world")

def list_all(request):
	all_lists = List.objects.all()
	return HttpResponse(all_lists)

def add_list(request):
	return HttpResponse("this is where you add lists")

def list(request, title):
	return HttpResponse("this is a page for a list %s" % title)


