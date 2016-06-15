from django.shortcuts import render , redirect
from django.http import request
from django.template.loader import render_to_string

from .forms import LoginForm
from .ldapops import LdapAuth
from django.core.urlresolvers import reverse

# Create your views here.

def chpasswd(request):
    loginForm = None
    if request.method == 'POST':
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            ldapAuth = LdapAuth()
            messages = ldapAuth.ldap_auth(request.POST['username'], request.POST['old_password'])
            if messages['status'] == 0: 
                ldapAuth.ldap_chpasswd(request.POST['username'], request.POST['new_password'])
                return redirect(request, reverse('success'))
    else:
        loginForm = LoginForm()
    return render(request, "ok.html", {"form":loginForm})

def ldap_auth(request):
    return render(request, "ok.html")

def success(request):
    return render("success.html")

