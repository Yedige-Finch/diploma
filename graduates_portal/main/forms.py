from django import forms

class login_form(forms.Form):
	# спросить насчет типа для айдишки
    student_id = forms.CharField(label='Your name', max_length=100)
    password = forms.CharField(label='Your password', max_length=100)
