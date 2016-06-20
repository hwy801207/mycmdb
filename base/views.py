from django.shortcuts import render, redirect
from django import forms
from .models import Resource, Server
from django.core.urlresolvers import reverse



class UploadForm(forms.Form):
    username = forms.CharField(label="username", max_length=120)
    file = forms.FileField()
# Create your views here.
def upload(request):
    uf = None
    if request.method == "POST":
        uf = UploadForm(request.POST, request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            file = uf.cleaned_data['file']
            rs = Resource()
            rs.username = username
            rs.file_path = file
            rs.save()
        return redirect("/resource/upload") 
    else:
        uf = UploadForm()
        #下载列表数据  data = download_list
        data = Resource.objects.all()
        return render(request, 'upload.html', {"uf":uf, "data": data})

def download(request):
    pass

#关于server
def addServer(request):
    if request.method == 'POST':
        hostname, ipAddr, machineType = request.POST['hostname', 'ipaddr', 'machinetype']
        server = Server();
        server.hostname = hostname
        server.ipAddr = ipAddr
        server.type = machineType
        server.save()
        return redirect(reverse('query'))
    else: 
        return render(request, 'server/add.html')

def modifyServer(request):
    pass

def delServer(request):
    pass

def getServer(request):
    pass
