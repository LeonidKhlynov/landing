from django.shortcuts import render
from django.shortcuts import redirect
from .models import *

def home_page(request):
	news = New.objects.order_by('id')
	return render(request, 'landingpage/main.html', {'news': news})