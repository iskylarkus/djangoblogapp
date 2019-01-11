from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.


def user_register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        new = User(username=username)
        new.set_password(password)
        new.save()

        login(request, new)
        messages.success(request, 'Başarıyla kayıt oldunuz..!')
        return redirect("index")
    else:
        context = {
            "form": form
        }
        return render(request, "user_register.html", context)

    """
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            new = User(username=username)
            new.set_password(password)
            new.save()

            login(request, new)
            return redirect("index")
        else:
            context = {
                "form": form
            }
            return render(request, "user_register.html", context)
    else:
        form = RegisterForm()
        context = {
            "form": form
        }
        return render(request, "user_register.html", context)"""

    """
    form = RegisterForm()
    context = {
        "form": form
    }
    return render(request, "user_register.html", context)"""


def user_login(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Kullanıcı adı veya parola hatalı...!")
            return render(request, "user_login.html", context)
        else:
            messages.success(request, 'Başarıyla giriş yaptınız..!')
            login(request, user)
            return redirect("index")
    else:
        return render(request, "user_login.html", context)


def user_logout(request):
    logout(request)
    messages.success(request, 'Başarıyla çıkış yaptınız..!')
    return redirect("index")
