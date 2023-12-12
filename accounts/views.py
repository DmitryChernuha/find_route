from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from accounts.forms import UserLoginForm


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect()
    return render(request, 'accounts/login.html', {'form': form})







