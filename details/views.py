from django.shortcuts import render,HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.

#this function will add new items amd show all items
def add(request):
    if request.method=='POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['Email']
            pw=fm.cleaned_data['password']
            reg = User(name=nm,Email=em,password=pw)
            reg.save()
            fm=StudentRegistration()
    else:
        fm=StudentRegistration()
    stud=User.objects.all()
    return render(request,'adddetails.html',{'forms':fm,'stu':stud})

#this function will edit/update
def update_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=User.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request, 'updatedetails.html',{'form':fm})

        
#this function will delete data
def delete_data(request,id):
    if request.method=='POST':
        pi=User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
           