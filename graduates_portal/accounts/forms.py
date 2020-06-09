from django import forms
from django.forms import ModelForm
# from .models import Student,Employer,User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field

# class UserForm(UserCreationForm):
	
# 	password = forms.CharField(widget=forms.PasswordInput())
# 	password_confirm = forms.CharField(widget=forms.PasswordInput())
	
# 	class Meta:
# 	    model = User
# 	    fields = ('first_name','last_name', 'email','password')

# 	def clean_last_name(self):
# 		if len(str(self.cleaned_data.get('last_name')).strip())!=0:
# 			lastname=str(self.cleaned_data.get('last_name')).lower()
# 			lastname=lastname[0].upper()+lastname[1:]
# 			if len(lastname)<1:
# 				raise forms.ValidationError('Обязательное поле')
# 			return lastname
# 		else:
# 			raise forms.ValidationError('Обязательное поле')

# 	def clean_first_name(self):
# 		if len(str(self.cleaned_data.get('first_name')).strip())!=0:
# 			firstname=self.cleaned_data.get('first_name').lower()
# 			firstname=firstname[0].upper()+firstname[1:]
# 			if len(firstname)<1 or firstname=="":
# 				raise forms.ValidationError('Обязательное поле')
# 				re.split(r'^[0-9_~!@#$%^&*()=+\.,/|[]{}''""><:;?]+$--', firstname)
# 			return firstname
# 		else:
# 			raise forms.ValidationError('Обязательное поле')

# 	def clean_email(self):
# 		email=self.cleaned_data.get('email')
# 		if len(email)<5:
# 			raise forms.ValidationError('Обязательное поле')
# 		return email

# 	def clean_password(self):
# 		email=self.cleaned_data.get('password')
# 		if len(email)<8:
# 			raise forms.ValidationError('Должно быть не менее 7 символов')
# 		return email

# 	def save(self, commit=True):
# 		user = super(UserForm, self).save(commit=False)
# 		user.username = str(self.cleaned_data.get('email'))
# 		if commit:
# 			user.save()
# 			return user

# 	def clean(self):
# 		cleaned_data = super(UserForm, self).clean()
# 		email = self.cleaned_data.get('email')
# 		password = cleaned_data.get("password")
# 		password_confirm = cleaned_data.get("password_confirm")
# 		user = email
# 		if User.objects.filter(username=str(user)).exists():
# 			raise forms.ValidationError('Почта уже используется!')
# 		if password != password_confirm:
# 			raise forms.ValidationError("Пароли не совпадают")


# class StudentForm(ModelForm):
#     class Meta:
#         model = Student
#         fields = ('student_id', 'course', 'speciality', 'phone')
        

# class EmployerForm(ModelForm):
#     class Meta:
#         model = Employer
#         fields = ('org_name','position','phone')

