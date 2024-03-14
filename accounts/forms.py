from typing import Any
from django import forms
from .models import User , OtpCode
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField

class UserCreateForm(forms.ModelForm):
    password1 = forms.CharField(label='password' , widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password' , widget=forms.PasswordInput)


    class Meta:
        model  = User
        fields = ('email' , 'phone_number' , 'full_name')

        def clean_password2(self):
            cd =self.clean_data
            if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2'] :
                raise ValidationError('the password is not same')
            return cd['password2']
        
        def save(self, commit=True):
            user = super().save(commit=False)
            user = set_password(self.clean_data['password1'])
            if commit:
                user.save()
            return user
        
class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField(help_text="you can change password using <a href = \"../password/\"> this form </a>")

    class Meta:
        model=User
        fields = ('email' , 'phone_number' , 'full_name')


class UserRegisterationForm(forms.Form):
     email=forms.EmailField()
     phone_number=forms.CharField(max_length=11)
     full_name=forms.CharField(label='full name')
     password = forms.CharField(widget=forms.PasswordInput)

     def clean_email(self):
         email = self.cleaned_data['email']
         user = User.objects.filter(email = email ).exists()
         if user :
             ValidationError('this email already exists.')
         return email
     
     def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        user = User.objects.filter(phone_number = phone_number ).exists()
        if user :
            ValidationError('this phone already exists.')
        OtpCode.objects.filter(phone_number=phone).delete()
        return phone_number

class VerifyCodeForm(forms.Form):
    code = forms.IntegerField()

class UserLoginForm(forms.Form):
	phone = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

   