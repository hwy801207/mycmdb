from django.shortcuts import render, redirect
from django import forms
from .models import Resource, Server
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse



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
        hostname = request.POST['hostname']
        ipAddr = request.POST['ipaddr']
        machineType = request.POST['machinetype']
        server = Server();
        server.hostname = hostname
        server.ipAddr = ipAddr
        server.type = machineType
        server.save()
        return redirect(reverse('listserver'))
    else: 
        return render(request, 'server/add.html')

def modifyServer(request, serverId=None):
    '''
        change server info by server id
    '''
    if request.method == 'POST':
        hostname = request.POST['hostname']
        ipAddr = request.POST['ipaddr']
        machineType = request.POST['machinetype']
        serverId = request.POST['serverid']
        server = Server.objects.get(id=serverId)
        server.hostname = hostname
        server.ipAddr = ipAddr
        server.type = machineType
        server.save()
        return redirect(reverse('listserver'))
    else:
        server = None
        if (serverId != None):
            server = Server.objects.get(id=serverId)
        return render(request, 'server/edit.html', {"server":server})

def delServer(request, serverId=None):
    '''
    del server by serverid
    '''
    if serverId != None:
        try:
            server = Server.objects.get(id=serverId)
            if server != None:
                server.delete()
        except Exception as e:
            print(e)
    return redirect(reverse('listserver'))

def getServer(request):
    '''
    get all server info list not by pager
    '''
    servers = Server.objects.all()
    return render(request, "server/list.html", {"servers":servers})

