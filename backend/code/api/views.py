from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Port, Trip
from api.serializers import PortSerializer, TripSerializer
from datetime import datetime, timedelta
import logging
from django.db.models import Q
from api.utils import calculate_path

@csrf_exempt
def best_path(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        src = data['src']
        toVisit = data['toVisit']
        vacationDays = data['vacationDays']
        startDate = datetime(2019,1,1)
        filters = data['filters']
        responseData = {
            'cheap': calculate_path('cheap', src, toVisit, startDate, vacationDays, filters),
            'fast': calculate_path('fast', src, toVisit, startDate, vacationDays, filters),
            'balanced': calculate_path('balanced', src, toVisit, startDate, vacationDays, filters)
        }
        return JsonResponse(responseData, safe=False)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)

