from django import forms
from .models import LoginUser
from captcha.fields import CaptchaField


class UserForm(forms.Form):
    username = forms.CharField(label="用户", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')

class RegisterForm(forms.Form):
    gender = (
        ('male', "male"),
        ('female', "female"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')

class HomeForm(forms.ModelForm):
    class Meta:
        model = LoginUser
        fields = ['username', 'password', 'email', 'info_right']
    info_right = forms.CharField(label="账户类型", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
#    subinfor = forms.CharField(label="下属", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))

class ChangePassForm(forms.ModelForm):
    class Meta:
        model = LoginUser
        fields = ['password', 'new_password1', 'new_password2']
    password = forms.CharField(label="旧密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label="新密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label="确认新密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
