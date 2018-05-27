from django.shortcuts import render
# Create your views here.
from chatting.models import *



def index(request):
		return render(request, 'main.html')
