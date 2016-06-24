from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    return render(request, "index.html");

def about(request):
    return HttpResponse("上海阅客信息科技有限公司")
