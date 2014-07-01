from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.shortcuts import render_to_response
from django.template import RequestContext

from accounts.forms import AccountForm


def accounts(request):
    account = request.user.account
    account_form = AccountForm(instance=account)
    user_form = UserChangeForm(instance=request.user)
    password_form = PasswordChangeForm(user=request.user)

    return render_to_response(
        'accounts/index.html',
        locals(),
        context_instance=RequestContext(request)
    )


def Login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
        else:
            print 'Disabled'
    else:
        print 'invalid login'


def Logout(request):
    logout(request)
    return render_to_response(
        'index.html',
        locals(),
        context_instance=RequestContext(request)
    )
