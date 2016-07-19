from django.shortcuts import render, redirect
# Create your views here.
from ldap.ldapops import LdapAuth
from django.contrib.auth.views import logout

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        ldapAuth = LdapAuth()
        is_authed = ldapAuth.ldap_auth(username, password)
        if is_authed: #if authed success make session store login status for 10 day
            request.session['user'] = username;
            return redirect("/")
    return render(request, 'login.html')


def logout_view(request):
    logout(request);
    return render(request, 'index.html')
