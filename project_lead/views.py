
from django.shortcuts import render,redirect
from django.http import HttpResponse
# from project_lead.models import Personal
from project_lead.LeadAlgo import AnalysisAlgo

def index(request):
    # data=Personal.objects.all()
    # context={'personals':data}
    # return render(request,'personal/home.html',context)
    return render(request,"project_lead/index.html")

def analysis(request):
    data=[request.POST['data']]
    print(AnalysisAlgo(data))
    # # personal.name=request.POST['name'] add like this
    # personal=Personal(name=request.POST['name'],email=request.POST['email'],contect=request.POST['contect'])
    # personal.save()
    return redirect('/')