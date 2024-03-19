from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import *


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
