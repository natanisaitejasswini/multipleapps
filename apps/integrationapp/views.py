from django.shortcuts import render
from django.core.urlresolvers import reverse
from .models import User_Add
from django.db.models import Count
from ..courseapp.models import Course
from ..loginregapp.models import Userlog
def index(request):
	context = {
		'courses': Course.objects.all().annotate(courseusers = Count("courses")),
		'users': Userlog.objects.all(),
	}
	return render(request,'integrationapp/index.html',context)
def add_newuser(request):
	user = Userlog.objects.get(id = request.POST['userid'])
	print user
	course = Course.objects.get(id = request.POST['courseid'])
	User_Add.objects.create(course_id=course.id, user_id=user.id)
	return redirect('/adder')