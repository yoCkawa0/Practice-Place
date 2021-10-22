# from django.shortcuts import render

# Create your views here.


# from django.http import HttpResponse

from django.shortcuts import render

def index(request):
    # top page
    content = {
        'name':'Yoshikatsu'
    }
    return render(request,'myapp/index.html',content)


def about(request):
    # about page
    return render(request,'myapp/about.html')

def info(request):
    # info page
    return render(request,'myapp/info.html')
