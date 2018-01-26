from django.shortcuts import render
from django.shortcuts import redirect
from .forms import *
from .models import *

def home_page(request):
	news = New.objects.order_by('id')
	if request.method == "POST":
		form = AppForm(request.POST)
		if form.is_valid():
			application = form.save(commit=False)
			application.fio != ''
			application.phone != ''
			application.email != ''
			application.works != ''
			application.comment != ''
			application.save()
			return redirect('/')
	else:
		form = AppForm()
	work_list = Work.objects.order_by('work_type')
	work_cont = {'work_list': work_list, 'form': form}
	return render(request, 'landingpage/main.html', work_cont)
	return render(request, 'landingpage/main.html', {'news': news})

	