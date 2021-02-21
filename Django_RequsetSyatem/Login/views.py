import hashlib
from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from . import models
from . import forms
from .forms import UserForm,RegisterForm

# Create your views here.

def hash_code(s, hk='lxf'):
    h = hashlib.sha256()
    s += hk
    h.update(s.encode())
    return h.hexdigest()

def login(request):
    if request.session.get('is_login') == True:
        return redirect('/index/')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查输入内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.username
                return redirect('/index/')
            else:
                 message = "用户名或者密码不对"
                 return render(request, 'login/login.html', locals())
        return render(request, 'login/login.html', locals())
    login_form = UserForm()
    return render(request,'login/login.html', locals())

def register(request):
    if request.session.get('is_login') == True:
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查输入内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2:
                message = "两次输入密码不一致！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.LoginUser.objects.filter(username=username)
                if same_name_user:
                    message = "用户名已存在，请换一个！"
                    return render(request, 'login/register.html', locals())
                same_email_user = models.LoginUser.objects.filter(email=email)
                if same_email_user:
                    message = "邮箱已经被使用，请换一个！"
                    return render(request, 'login/register.html', locals())
                new_user = models.LoginUser()
                new_user.username = username
                new_user.password = make_password(password1)
                new_user.email = email
                new_user.save()
                return redirect('/login/')
    register_form = RegisterForm()
    return render(request,'login/register.html', locals())

def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/index/")
    request.session.flush()
    return redirect('/index/')

def HomePage(request):
    if request.session.get('is_login') == None:
        return render(request, 'LoginWarning.html', locals())
    user = request.session['user_name']
    user_model = models.LoginUser.objects.get(username=user)
    form = forms.HomeForm()
    user_form = forms.HomeForm(instance=user_model)
    return render(request, 'login/homepage.html', locals())

def ModUser(request):
    if request.session.get('is_login') == None:
        return render(request, 'LoginWarning.html', locals())
    user = request.session['user_name']
    user_model = models.LoginUser.objects.get(username=user)
    if request.method == "POST":
        change_form = forms.ChangePassForm(request.POST, instance=user_model)
        message = "please check in the content!"
        if change_form.is_valid():
            old_password = change_form.cleaned_data['password']
            new_password1 = change_form.cleaned_data['new_password1']
            new_password2 = change_form.cleaned_data['new_password2']
            if user_model.check_password(old_password, user_model.password):
                if new_password1 == new_password2:
                    user_model.password = make_password(new_password1)
                    user_model.save()
                    return render(request, 'login/homepage.html', locals())
                else:
                    message = '两次输入密码不一致'
                    return render(request, 'login/moduser.html', locals())
            else:
                message = '原密码不对'
                return render(request, 'login/moduser.html', locals())
    else:
        change_form = forms.ChangePassForm(request.POST, instance=user_model)
    return render(request, 'login/moduser.html', locals())

def WebHome(request):
    return render(request,'login/webhome.html', locals())
