from django.http import HttpResponse
from django.shortcuts import render
def aboutus(request):
    return HttpResponse("for the fun and talaf")
        

def homepage(request):
    return render(request,"homepage.html")

def index(request):
    return render(request,"index.html")

def course(request):
    data={
        'title':'homepage',
        'body':'homePage',
        'clist':['php','sql','python'],
        'number':[],
        'student':[
        {'rollno':2,'name':'akash'},
        {'rollno':4,'name':'namashivam'}
        ]
        
        
    }
    def index(request):
        return render(request,'index.html',)
 