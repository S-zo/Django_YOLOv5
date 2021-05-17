from django.shortcuts import render

from time import time
from pybo.models import Photos2, Count, Ke, Km
from video.models import Mfl

from django.views.generic import View
from django.http import JsonResponse


# Create your views here.
def base(request):
    return render(request, 'index.html')

def photos(request):
    photos = Photos2.objects.all()
    return render(request, 'photos.html', {'photos': photos})

#########################################
class ajax_test(View):
    def get(self, request):
        # text = request.GET.get('button_text')
        
        if request.is_ajax():
            
            smoke = Count.objects.values('smoke')
            nohelmet = Count.objects.values('nohelmet')
            nomask = Count.objects.values('nomask')
            danger = Count.objects.values('danger')
            human = Count.objects.values('human')
            
            # # sensor3=model_to_dict(sensor3)
            
            smoke = smoke[0]
            nohelmet = nohelmet[0]
            nomask = nomask[0]
            danger = danger[0]
            human = human[0]
            
            smoke = smoke['smoke']
            nohelmet = nohelmet['nohelmet']
            nomask = nomask['nomask']
            danger = danger['danger']
            human = human['human']

            return JsonResponse({'smoke': smoke, 'nohelmet': nohelmet, 'nomask': nomask, 'danger': danger, 'human': human}, status=200)

        return render(request, 'for_ajax.html')

def first(request):
    return render(request, 'first.html')

def wait(request):
    return render(request, 'waitaminute.html')
    
def socket(request):
    return render(request, 'socket_test.html')
    
    
def dashboard(request):
    return render(request, 'dashboard.html')


def issue(request):
    return render(request, 'issue.html')

def cctv(request):
    return render(request, 'cctv.html')


def mapping(request):
    return render(request, 'map.html')

def contact(request):
    return render(request, 'contact.html')

def form(request):
    return render(request, 'form.html')

def shop(request):
    return render(request, 'shop.html')

def about(request):
    return render(request, 'about.html')

def sensor(request):
    
    m_sensor_1=[]
    m_sensor_2=[]
    m_sensor_3=[]
    m_sensor_4=[]
    m_sensor_5=[]
    m_sensor_6=[]
    m_id_data=[]
    
    for i in range(18754):
        m_id_data.append(i)
        

    m_sensor1 = Km.objects.values('sensor1')
    m_sensor2 = Km.objects.values('sensor2')
    m_sensor3 = Km.objects.values('sensor3')
    m_sensor4 = Km.objects.values('sensor4')
    m_sensor5 = Km.objects.values('sensor5')
    m_sensor6 = Km.objects.values('sensor6')
    
    count=0
    for sensor in m_sensor1:
        m_sensor_1.append(sensor["sensor1"])

    for sensor in m_sensor2:
        m_sensor_2.append(sensor["sensor2"])
    for sensor in m_sensor3:
        m_sensor_3.append(sensor["sensor3"])
    for sensor in m_sensor4:
        m_sensor_4.append(sensor["sensor4"])
    for sensor in m_sensor5:
        m_sensor_5.append(sensor["sensor5"])
    for sensor in m_sensor6:
        m_sensor_6.append(sensor["sensor6"])

    m_line_chart = [m_id_data, m_sensor_1, m_sensor_2, m_sensor_3, m_sensor_4, m_sensor_5, m_sensor_6]
    

    e_sensor_1=[]
    e_sensor_2=[]
    e_sensor_3=[]
    e_sensor_4=[]
    e_sensor_5=[]

    e_id_data=[]
    
    for i in range(19000):
        e_id_data.append(i)


    e_sensor1 = Ke.objects.values('sensor1')
    e_sensor2 = Ke.objects.values('sensor2')
    e_sensor3 = Ke.objects.values('sensor3')
    e_sensor4 = Ke.objects.values('sensor4')
    e_sensor5 = Ke.objects.values('sensor5')

    count=0
    for sensor in e_sensor1:
        e_sensor_1.append(sensor["sensor1"])
        
        count+=1
        if count==19000:
            break

    for sensor in e_sensor2:
        e_sensor_2.append(sensor["sensor2"])
        
        count+=1
        if count==19000:
            break


    for sensor in e_sensor3:
        e_sensor_3.append(sensor["sensor3"])
        
        count+=1
        if count==19000:
            break
     
    for sensor in e_sensor4:
        e_sensor_4.append(sensor["sensor4"])
        
        count+=1
        if count==19000:
            break
  
    for sensor in e_sensor5:
        e_sensor_5.append(sensor["sensor5"])
        
        count+=1
        if count==19000:
            break
 


    e_line_chart = [e_id_data, e_sensor_1, e_sensor_2, e_sensor_3, e_sensor_4, e_sensor_5]
    
    
    
    return render(request, 'sensor.html', {'e_line_chart' : e_line_chart, 'm_line_chart' : m_line_chart})