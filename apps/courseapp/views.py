from django.shortcuts import render, redirect
from .models import Course
from ..loginregapp.models import Userlog
def index(request):
	context = {
	"courses" : Course.objects.all(),
	"users"	: Userlog.objects.all()
	}
	return render(request,'courseapp/index.html', context)
		
def user(request):
	print request.POST
	new_course = Course()
	new_course.name = request.POST['name']
	new_course.description = request.POST['description']
	new_course.save()
	# Course.objects.create(name=request.POST['name'], description=request.POST['description'])
	return redirect('/courses')
def deletepage(request, id):
	context = {
	"course" : Course.objects.get(id = id)
	}
	return render(request,'courseapp/success.html',context)
def selectyes(request, id):
	course = Course.objects.get(id=id)
	course.delete()
	print request.POST
	return redirect('/courses')


















