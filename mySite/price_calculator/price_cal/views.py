from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.

def index(request):
	return render(request,'',context)