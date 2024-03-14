from django.shortcuts import render , redirect
from django.views import View
from .forms import UserRegisterationForm , VerifyCodeForm , UserLoginForm
import random
from .models import OtpCode , User
from  utils import send_otp_code
from django.contrib import messages
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.mixins import LoginRequiredMixin

class UserRegisterView(View):
    class_form = UserRegisterationForm
    template_name = 'accounts/register.html'

    def get(self , request):
        form = self.class_form
        return render(request , self.template_name , {'form':form})

    def post(self , request):
        form = self.class_form(request.POST)
        if form.is_valid():
            random_code = random.randint(1000 , 9999)
            send_otp_code(form.cleaned_data['phone_number'] , random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'] , code =random_code)
            request.session['user_registeration_info'] = {
                'phone_number':form.cleaned_data['phone_number'] ,
                'email': form.cleaned_data['email'] ,
                'full_name' : form.cleaned_data['full_name'] ,
                'password' : form.cleaned_data['password'] ,  
            }

            messages.success( request, 'we sent code for you' , 'success' )
            return redirect('accounts:verify_code')
        # else:
        #     raise ValidationError(
        #         _("Invalid value: %(value)s"),
        #             code="invalid",
        #             params={"value": "42"},)
        return render(request ,  self.template_name , {'form':form})
    
    
class UserRegisterVerifyCodeView(View):
    form_class = VerifyCodeForm

    def get(self , request ):
        form = self.form_class
        return render(request , 'accounts/verify.html' , {'form':form})
        # print('='*90)
        # print(user_session)

    def post(self , request ):
        user_session = request.session['user_registeration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code :
                User.objects.create_user(user_session['phone_number'] , user_session['email'] , 
                                         user_session['full_name'] , user_session['password'])
                
                code_instance.delete()
                messages.success(request , 'you registerd' , 'danger')
                return redirect('home:home')
            else:
                messages.error(request , 'the code is wrong' , 'danger')
                return redirect('accounts:verify_code')
        return redirect('accounts:verify_code')

class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you logged out successfully', 'success')
        return redirect('home:home')


class UserLoginView(View):
	form_class = UserLoginForm
	template_name = 'accounts/login.html'

	def get(self, request):
		form = self.form_class
		return render(request, self.template_name, {'form':form})

	def post(self, request):
		form = self.form_class(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			user = authenticate(request, phone_number=cd['phone'], password=cd['password'])
			if user is not None:
				login(request, user)
				messages.success(request, 'you logged in successfully', 'info')
				return redirect('home:home')
			messages.error(request, 'phone or password is wrong', 'warning')
		return render(request, self.template_name, {'form':form})