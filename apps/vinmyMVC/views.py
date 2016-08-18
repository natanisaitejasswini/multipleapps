from django.shortcuts import render, redirect
import random
from datetime import datetime
def index(request):
	if 'totalgold' not in request.session or 'activities' not in request.session:
		request.session['totalgold'] = 0
		request.session['activities'] = []
	return render(request,'vinmyMVC/index.html')
def create(request):
	print request.method
	if request.method == "POST":
		print request.session.items()
		print request.POST
		if request.POST['building'] == 'Farm':
			print 50*'*'
			newgold = random.randint(10,20)
		elif request.POST['building'] == 'Cave':
			newgold = random.randint(5,10)
		elif request.POST['building'] == 'House':
			newgold = random.randint(2,5)
		elif request.POST['building'] == 'Casino':
			newgold = random.randint(-50,50)
		request.session[ 'totalgold' ] += newgold
		if newgold > 0:
			request.session['activities'].append( "<span class ='win'> You've earned {} golds from the {}! ({})</span>".format(newgold,request.POST['building'], datetime.now().strftime("%Y/%m/%d, %X")))
		if newgold < 0:
			request.session['activities'].append("<span class ='lost'> Entered a casino and lost {} golds...Ouch...({})</span>".format(newgold, datetime.now().strftime("%Y/%m/%d, %X")))
		return redirect('/ninjas')
	else:
		return redirect('/ninjas')
def gold_refresh(request):
	del request.session['totalgold']
	del request.session['activities']
   	return redirect('/ninjas')