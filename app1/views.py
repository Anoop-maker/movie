from django.shortcuts import render
from app1.models import Movies

# Create your views here.
def home(request):
    k=Movies.objects.all()
    context={'movies':k}
    return render(request,'home.html',context)

def add(request):
    if(request.method=='POST'):
        t=request.POST['t']
        d = request.POST['d']
        y = request.POST['y']
        l = request.POST['l']
        i = request.FILES.get('i')
        m=Movies.objects.create(title=t,desc=d,year=y,language=l,image=i)
        m.save()
        return home(request)
    return render(request,'add.html')

def details(request,i):
    k=Movies.objects.get(id=i)
    context={'movies':k}
    return render(request,'details.html',context)

def delete(request,i):
    k=Movies.objects.get(id=i)
    k.delete()
    return home(request)

def edit(request,i):
    k = Movies.objects.get(id=i)
    if(request.method=='POST'):
        k=Movies.objects.get(id=i)
        k.title=request.POST['t']
        k.desc = request.POST['d']
        k.year = request.POST['y']
        k.language = request.POST['l']

        if(request.FILES.get('i')==None):
            k.save()
        else:
            k.image=request.FILES.get('i')
        k.save()
        return home(request)

    return render(request,'edit.html',{'movies':k})