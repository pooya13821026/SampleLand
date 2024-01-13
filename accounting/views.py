from django.contrib.auth import login, logout
from django.http import HttpRequest, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.views import View
from .forms import RegisterForm, LoginForm, ForgetPassForm, ResetPassForm
from .models import User
from utilities.email_services import send_email


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'accounting/register_page.html', context)

    def post(self, request: HttpRequest):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_email = register_form.cleaned_data.get('email')
            user_pass = register_form.cleaned_data.get('password')
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل تکراری میباشد')
            else:
                registered_user = User(email=user_email, email_active_code=get_random_string(72), username=user_email)
                registered_user.set_password(user_pass)
                registered_user.save()
                login(request, registered_user)
                # send_email('فعالسازی حساب کاربری', user_email, {'user': user}, 'email/active_account.html')
            return redirect(reverse('dashboard'))
        context = {
            'register_form': register_form
        }
        return render(request, 'accounting/register_page.html', context)


class LoginView(View):
    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'accounting/login_page.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            entered_email = login_form.cleaned_data.get('email')
            entered_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=entered_email).first()
            if user is not None:
                if user.is_active:
                    check_pass = user.check_password(entered_pass)
                    if check_pass:
                        login(request, user)
                        return redirect(reverse('home_page'))  # redirect to dashboard

                else:
                    login_form.add_error('email', 'حساب کاربری شما فعال نیست')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')

        context = {
            'login_form': login_form
        }
        return render(request, 'accounting/login_page.html', context)


class ActiveEmailAccountView(View):  # Send success message to user
    def get(self, request, email_activate_code):
        user: User = User.objects.filter(email_active_code__iexact=email_activate_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                return redirect(reverse('login_page'))

        raise Http404


class ForgetPassView(View):
    def get(self, request):
        forget_form = ForgetPassForm()
        context = {
            'forget_form': forget_form
        }
        return render(request, 'accounting/forget_pass_page.html', context)

    def post(self, request: HttpRequest):
        forget_form = ForgetPassForm(request.POST)
        if forget_form.is_valid():
            email = forget_form.cleaned_data.get('email')
            user: User = User.objects.filter(email__iexact=email).first()
            if user is not None:
                send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'email/reset_password.html')
            context = {
                'forget_form': forget_form
            }
            return render(request, 'accounting/forget_pass_page.html', context)

        context = {
            'forget_form': forget_form
        }
        return render(request, 'accounting/forget_pass_page.html', context)


class ResetPassView(View):
    def get(self, request, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('register_page'))
        reset_form = ResetPassForm()
        context = {
            'reset_form': reset_form,
        }
        return render(request, 'accounting/reset_pass_page.html', context)

    def post(self, request: HttpRequest, active_code):
        reset_form = ResetPassForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_form.is_valid():
            if user is None:
                return redirect(reverse('register_page'))
            else:
                user_pass = reset_form.cleaned_data.get('password')
                user.set_password(user_pass)
                user.email_active_code = get_random_string(72)
                user.is_active = True
                user.save()
                return redirect(reverse('login_page'))

        context = {
            'reset_form': reset_form,
            'user': user
        }
        return render(request, 'accounting/reset_pass_page.html', context)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login_page'))
