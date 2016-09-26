from django.shortcuts import render
from .models import List, List_Item

# Create your views here.
def index(request):
	latest_lists = List.objects.all('-date')[:10]
	context = {'latest_lists': latest_lists}
	return render(request, 'lists/index.html', context)

def list_all(request):
	pass	

def add_list(request):
	return render(request, 'lists/add_list.html', {})

def list(request, title):
	return HttpResponse("this is a page for a list %s" % title)


