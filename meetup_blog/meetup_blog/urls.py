"""meetup_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import render,redirect
# from django.contrib.auth.forms import AdminPasswordChangeForm
from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control'
    }))
    email = forms.EmailField(required=False)
    phone_number = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        if email != 'gbozee@example.com':
            self.add_error('email',"This email is invalid")
        return email




def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, 'login.html')

def register(request):
    register_form = SignupForm()
    if request.method == 'POST':
        register_form = SignupForm(request.POST)
        if register_form.is_valid():
            return redirect('home')
    return render(request, 'signup.html',{'form':register_form,'none':None})


urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^login/$', login, name='login'),
    url(r'^signup/$', register, name='signup'),
    url(r'^admin/', admin.site.urls),
]
