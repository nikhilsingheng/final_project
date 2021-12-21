#
# from django.shortcuts import render, redirect
# from django.contrib import messages
# from django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm
# # from django.core.mail import send_mail
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import get_template
# from django.template import Context
# import email
#
# from login import models
# from django.views.decorators.csrf import csrf_exempt
#
#
#
#
#
# from login.models import UsersignForm
#
#
# @csrf_exempt
# def index(request):
# 	return render(request, 'login/index.html', {'title':'index'})
#
#
# @csrf_exempt
#
# def sign(request):
# 	if request.method == 'POST':
# 		form = UsersignForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			email = form.cleaned_data.get('email')
# 			email = form.cleaned_data.get('email')
#
# 			htmly = get_template('template/sign.html')
# 			d = { 'email': email }
# 			subject, from_email, to = 'welcome', 'your_email@gmail.com', email
# 			html_content = htmly.render(d)
# 			msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
# 			msg.attach_alternative(html_content, "text/html")
# 			msg.send()
#
# 			messages.success(request, f'Your account has been created ! You are now able to log in')
# 			return redirect('login')
# 	else:
# 		form = UsersignForm()
# 	return render(request, 'template/sign.html', {'form': form, 'title':'reqister here'})
#
#
# @csrf_exempt
#
# def Login(request):
# 	if request.method == 'POST':
#
# 		# AuthenticationForm_can_also_be_used__
#
# 		username = request.POST['email']
# 		password = request.POST['password']
# 		user = authenticate(request, email = email, password = password)
# 		if user is not None:
# 			form = login(request, user)
# 			messages.success(request, f' wecome {email} !!')
# 			return redirect('index')
# 		else:
# 			messages.info(request, f'account done not exit plz sign in')
# 	form = AuthenticationForm()
# 	return render(request, 'template/sign.html', {'form':form, 'title':'log in'})
#
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from login import models
def index(request):
    return render(request,"login.html")
@csrf_exempt
def signup(request):

    return render(request, "sign.html")
@csrf_exempt
def Sign(request):
    email = request.POST.get('email')
    Password = request.POST.get('Password')
    repeat_Password = request.POST.get('repeat_Password')
    models.UsersignForm.objects.create(email=email, Password=Password, repeat_Password=repeat_Password)
    return HttpResponseRedirect('http://127.0.0.1:8000/Home/')
@csrf_exempt
def login(request):

    email = request.POST.get('email')
    Password = request.POST.get('Password')
    data =  models.UsersignForm.objects.get(email=email)
    if email== data.email and Password== data.Password:
        return HttpResponseRedirect('http://127.0.0.1:8000/Home/')


    else:
        return HttpResponse("error")
def Home(request):
    return render(request,"index.html")




