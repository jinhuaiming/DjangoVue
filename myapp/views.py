from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse
from .models import Argoheader, Argocore
import json


# Create your views here.
def index(request):
    return render(request, 'app/index.html')

# 根据浮标编号，查询浮标的所有周期信息
def queryPlaNum(request):
    platformnumber = request.GET.get('platformnumber')
    data = Argoheader.objects.filter(platformnumber=platformnumber)
    data_json = json.loads(serializers.serialize('json', data))
    position = []
    for item in data_json:
        position.append(item['fields']['longitude'])
        position.append(item['fields']['latitude'])
    position_data = [
        {platformnumber: position}
    ]
    return JsonResponse({
        'data': data_json,
        'position': position_data
    })

# 根据浮标编号和周期号，查询浮标某周期，测量的温度|盐度的数值
def handlePlot(request):
    pk = request.GET.get('pk')
    cyclenumber = request.GET.get('cyclenumber')
    data = Argocore.objects.filter(platformnumber=pk, cyclenumber=cyclenumber)
    data_json = json.loads(serializers.serialize('json', data))
    Depth = []
    Tem = []
    Sal = []
    for item in data_json:
        Depth.append(item['fields']['cpressure'])
        Tem.append(item['fields']['ctemperature'])
        Sal.append(item['fields']['csalinity'])
    Depth = Depth[::-1]
    Tem = Tem[::-1]
    Sal = Sal[::-1]

    return JsonResponse({
        'data': {
            'Depth': Depth,
            'Tem': Tem,
            'Sal': Sal
        }
    })

