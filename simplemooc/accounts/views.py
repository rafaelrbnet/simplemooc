from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import (UserCreationForm, PasswordChangeForm, SetPasswordForm)
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages

from simplemooc.core.utils import generate_hash_key
from simplemooc.courses.models import Enrollment

from .forms import RegisterForm, EditAccountForm, PasswordResetForm
from .models import PasswordReset


def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':  # modo não pratico para enviar as informações do post do formulario. veja abaixo como é mais fácil
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                username=user.username, password=form.cleaned_data['password1']
            )
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)


def password_reset(request):
    template_name = 'accounts/password_reset.html'
    context = {}
    form = PasswordResetForm(
        request.POST or None)  # forma especial para chamar o form com ou sem os parametros necessários do post
    if form.is_valid():
        form.save()
        messages.success(request, "Um e-mail foi enviado para você com mais detalhes de como criar uma nova senha")
        return redirect('accounts:dashboard')
    context['form'] = form
    return render(request, template_name, context)


def password_reset_confirm(request, key):
    template_name = 'accounts/password_reset_confirm.html'
    context = {}
    reset = get_object_or_404(PasswordReset, key=key)
    form = SetPasswordForm(user=reset.user, data=request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Sua senha foi criada com sucesso")
        return redirect('accounts:dashboard')
    context['form'] = form
    return render(request, template_name, context)


def logout(request):
    template_name = 'accounts/logout.html'
    return render(request, template_name)


''' este decorator verifica se relamente o usuario está logado'''


@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    return render(request, template_name)


@login_required
def edit(request):
    template_name = 'accounts/edit.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Os dados de sua conta foram alterados com sucesso")
            return redirect('accounts:dashboard')
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)


@login_required
def edit_password(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Sua senha foi alterada com sucesso")
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)
