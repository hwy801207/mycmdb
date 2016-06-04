from django.shortcuts import render
from django.http import request
from django.template.loader import render_to_string

# Create your views here.

def chpasswd(request):
    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['new_password'] 
        print(username, password)
    return render(request, "ok.html", {"u": username, "p":password})

def ldap_auth(request):
    return render(request, "ok.html")

