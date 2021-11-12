from django.shortcuts import render
from app.models import Service,Width

# Create your views here.
def index(request):
    serviceData=Service.objects.all().order_by('-service_title')[:2]
    
    # print(Service)
     
    data={
        # 'widthdata' : widthdata,
        'serviceData': serviceData
    }
    return render(request,'index.html',data)


def hello(request,subid):
    return render(request,'index.html')

def css(request):
    widthdata=Width.objects.all()

    data2={
        'widthdata' : widthdata,
    }

    return render(request,'index.html',data2)    




