from django.shortcuts import render,render_to_response,redirect
from . import views
from django.http import HttpResponse
# from .forms import login_form
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.
def main(request):
	return render_to_response('main.html')

# def login(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             login(request, user)
#             return redirect("main:main")
#         else:
#             for msg in form.error_messages:
#                 print(form.error_messages[msg])

#             return render(request,"home.html",{"form":form})

#     form = UserCreationForm
#     return render(request,"login.html",{"form":form})
   