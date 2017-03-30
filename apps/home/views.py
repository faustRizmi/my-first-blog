from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,render
from django.template import loader,Template,context ,RequestContext
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from apps.home.models import UsersAccount
from apps.home.forms import UsersAccountForm

# Create your views here.
def home(request):
	template = loader.get_template('home/home.html')
	return HttpResponse (template.render(request))


def signin(request):
	template = loader.get_template('home/signin.html')
	return HttpResponse (template.render(request))



def signup(request):
	if request.method == "POST":
		form = usersAccountForm(request.POST)
		if form.is_valid():
			post=form.save()
			post.save()
	else:
		form = usersAccountForm()
	return render(request,'home/signup.html',{'form': form})

