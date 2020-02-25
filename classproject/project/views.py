from django.shortcuts import render
from django.http import HttpResponse
from .models import Achievments,Testimonial,Form

# Create your views here.

def index(request):
    values=Achievments.objects.all()
    des = Testimonial.objects.all()
    len = Testimonial.objects.all().count()
    context={'values' : values,'des' : des, 'len': len}
    return render(request,'index.html',context)


def createpost(request):
        if request.method == 'POST':
            if request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('message'):
                post=Form()
                post.Name= request.POST.get('name')
                post.Email= request.POST.get('email')
                post.Message= request.POST.get('message')
                post.Phone_no= request.POST.get('phone')
                post.save()
                
                return render(request, 'contact.html')  

        else:
                return render(request,'contact.html')      


def about(request):
    return render(request,'about.html')   


def contact(request):
    return render(request,'contact.html') 


def portfolio(request):
    return render(request,'portfolio.html')    


