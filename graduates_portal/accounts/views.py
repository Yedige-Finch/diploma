from django.shortcuts import render,render_to_response,redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import auth
# from .forms import StudentForm,EmployerForm,UserForm
# from .models import Student,Employer,User
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.core.mail import send_mail
# Create your views here.


# def logout(request):
# 	auth.logout(request)
# 	print(auth.logout(request))
# 	return redirect('login')

# def login(request):
# 	context = {}
# 	if request.method == "POST":
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(request, username=username, password=password)
# 		print(user)
# 		if user is not None:
# 			if Student.objects.filter(user = User.objects.filter(username=username)[0])[0].сс_approve=='Y':
# 				auth.login(request,user)
# 				return redirect("main")
# 			else:
# 				context['text'] = 'Аккаунт еще не ободрен ЦК МУИТ'
# 				return render(request,"login.html",context)
# 		else:
# 			context['text'] = 'Логин или пароль неправильный'
# 			return render(request,"login.html",context)
# 	return render(request,"login.html",context)



# def registration_student(request):
# 	context = {}
# 	form = UserForm(request.POST or None)
# 	profile = StudentForm(request.POST or None)
# 	context['form'] = form
# 	context['profile'] = profile
# 	if request.method == "POST":
# 		if form.is_valid() and profile.is_valid():
# 			a = form.save()
# 			b = profile.save(commit=False)
# 			b.user = a
# 			b.save()
# 			user = User.objects.get(username=a)
# 			user.active=True
# 			user.save()
# 			return redirect("login")
# 	return render(request,"stud_form.html",context)

# def registration_employer(request):
# 	context = {}
# 	form = UserForm(request.POST or None)
# 	profile = EmployerForm(request.POST or None)
# 	context['form'] = form
# 	context['profile'] = profile
# 	if request.method == "POST":
# 		if form.is_valid() and profile.is_valid():
# 			a = form.save()
# 			b = profile.save(commit=False)
# 			b.user = a
# 			b.save()
# 			user = User.objects.get(username=a)
# 			user.save()
# 			return redirect("login")
# 	return render(request,"employer_form.html",context)



# from django.core.mail import send_mail
# import os
# def send_email_ska(request):
# 	send_mail('Subject here', 'Here is the message.', 'Project Test <no-reply@proj-test.kz>', ['edige87@gmail.com'], fail_silently=False)
# 	return redirect('main')
