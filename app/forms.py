from django import forms
from django.contrib.auth.forms import (UserCreationForm , AuthenticationForm ,UsernameField, PasswordChangeForm,
PasswordResetForm, SetPasswordForm)
from django.contrib.auth.models import User
from django.utils.translation import gettext , gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer, Product, Orderplaced

class UserRegistrationForm(UserCreationForm):
	username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'class':'form-control'}))
	password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
	email =	forms.EmailField(label="Email",required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))

	class Meta:
		model = User
		fields = ['username','password1','password2','email']

class LoginForm(AuthenticationForm):
	username = UsernameField(widget=forms.TextInput(attrs={ 'autofocus':True,'class':'form-control'}))
	password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={ 'autocomplete':'current-password','class':'form-control'}))

class MyPasswordChangeForm(PasswordChangeForm):
	old_password = forms.CharField(label=_("Old Password"),strip=False,widget=forms.PasswordInput(attrs=
		{ 'autofocus': True, 'autocomplete':'current-password','class':'form-control'}))
	new_password1 = forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs=
		{'autocomplete':'new-password','class':'form-control'}),
	help_text=password_validation.password_validators_help_text_html())
	new_password2 = forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs=
		{'autocomplete':'new-password','class':'form-control'}))

class MyPasswordResetForm(PasswordResetForm):
	email =	forms.EmailField(label=_("Email"),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'current-email','class':'form-control'}))

class MySetPasswordResetForm(SetPasswordForm):
	new_password1 = forms.CharField(label=_("New Password"),strip=False,widget=forms.PasswordInput(attrs=
		{'autocomplete':'new-password','class':'form-control'}),
	help_text=password_validation.password_validators_help_text_html())
	new_password2 = forms.CharField(label=_("Confirm New Password"),strip=False,widget=forms.PasswordInput(attrs=
		{'autocomplete':'new-password','class':'form-control'}))

class CustomerProfileForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = ['name','locality','city','state','zipcode']
		widgets = {'name': forms.TextInput(attrs={'class':'form-control'}),
		'locality': forms.TextInput(attrs={'class':'form-control'}),
		'city' : forms.TextInput(attrs={'class':'form-control'}),
		'state' : forms.Select(attrs={'class':'form-control'}),
		'zipcode' : forms.NumberInput(attrs={'class':'form-control'}),
		}

class ProductCreateForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = ['title','brand','discount_prize','selling_prize','category','description','product_image']
		widgets = {'title': forms.TextInput(attrs={'class':'form-control'}),
		'brand': forms.TextInput(attrs={'class':'form-control'}),
		'discount_prize' : forms.NumberInput(attrs={'class':'form-control'}),
		'selling_prize' : forms.NumberInput(attrs={'class':'form-control'}),
		'category' : forms.Select(attrs={'class':'form-control'}),
		'description' : forms.TextInput(attrs={'class':'form-control'}),
		'brand': forms.TextInput(attrs={'class':'form-control'}),
	    'product_image': forms.FileInput(attrs={'class':'form-control'}),
		}

class OrderUpdateForm(forms.ModelForm):
	class Meta:
		model = Orderplaced
		fields = ['status']