
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .HPP_MainModel import Predicate


def index(request):
    # data=Personal.objects.all()
    ab=[1,2,3,1,4,5]
    print('================',type(ab))
    cont={'val':ab}
    # context={'personals':data}
    # return render(request,'personal/home.html',context)
    return render(request,"project_lead/index.html",cont)

def analysis(request):
    data=[request.POST['data']]
    print(Predicate(data))

    context = {'val': Predicate(data),'Text':data}
    # # personal.name=request.POST['name'] add like this
    # personal=Personal(name=request.POST['name'],email=request.POST['email'],contect=request.POST['contect'])
    # personal.save()
    return render(request, "project_lead/result.html",context)