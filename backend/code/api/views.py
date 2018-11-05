from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Port, Trip
from api.serializers import PortSerializer, TripSerializer
from datetime import datetime, timedelta
from functools import reduce
import logging

@csrf_exempt
def best_path(request):
    src = 'Buenos Aires'
    toVisit = ['Paris', 'Londres', 'Barcelona']
    vacationDays = 7
    startDate = datetime(2019,1,1)
    if request.method == 'GET':
        """
            Cheap path
        """
        trips = []
        trip = Trip.objects.all(
            ).filter(fromPort__city=src
            ).filter(toPort__city__in=toVisit
            ).filter(departure__range=(startDate, startDate + timedelta(days=1))
            ).order_by('cost','duration'
            )[0]
        trips.append(trip)
        toVisit.remove(trip.toPort.city)
        lastTrip = trip
        while len(toVisit) > 0:
            trip = Trip.objects.all(
                ).filter(fromPort__city=lastTrip.toPort.city
                ).filter(toPort__city__in=toVisit
                ).filter(departure__range=(lastTrip.arrival, startDate + timedelta(days=vacationDays-len(toVisit)))
                ).order_by('cost','duration'
                )[0]
            trips.append(trip)
            toVisit.remove(trip.toPort.city)
            lastTrip = trip
        trip = Trip.objects.all(
            ).filter(fromPort__city=lastTrip.toPort.city
            ).filter(toPort__city=src
            ).filter(departure__gt=lastTrip.arrival
            ).filter(arrival__lt=startDate + timedelta(days=vacationDays)
            ).order_by('cost','duration'
            )[0]
        trips.append(trip)
        responseData = {}
        cheapResponseData = {}
        fastResponseData = {}
        balancedResponseData = {}
        serializer = TripSerializer(trips, many=True)
        totalCost = 0
        for trip in trips:
            totalCost += trip.cost
        cheapCost = totalCost
        cheapResponseData['totalCost'] = str(totalCost) + ' ' + lastTrip.currency
        totalDuration = timedelta()
        for trip in trips:
            totalDuration += trip.duration
        cheapResponseData['totalDuration'] = str(totalDuration)
        cheapResponseData['path']=serializer.data
        """
            Fast path
        """
        trips = []
        toVisit = ['Paris', 'Londres', 'Barcelona']
        trip = Trip.objects.all(
            ).filter(fromPort__city=src
            ).filter(toPort__city__in=toVisit
            ).filter(departure__range=(startDate, startDate + timedelta(days=1))
            ).order_by('duration','cost'
            )[0]
        trips.append(trip)
        toVisit.remove(trip.toPort.city)
        lastTrip = trip
        while len(toVisit) > 0:
            trip = Trip.objects.all(
                ).filter(fromPort__city=lastTrip.toPort.city
                ).filter(toPort__city__in=toVisit
                ).filter(departure__range=(lastTrip.arrival, startDate + timedelta(days=vacationDays-len(toVisit)))
                ).order_by('duration','cost'
                )[0]
            trips.append(trip)
            toVisit.remove(trip.toPort.city)
            lastTrip = trip
        trip = Trip.objects.all(
            ).filter(fromPort__city=lastTrip.toPort.city
            ).filter(toPort__city=src
            ).filter(departure__gt=lastTrip.arrival
            ).filter(arrival__lt=startDate + timedelta(days=vacationDays)
            ).order_by('duration','cost'
            )[0]
        trips.append(trip)
        responseData = {}
        serializer = TripSerializer(trips, many=True)
        totalCost = 0
        for trip in trips:
            totalCost += trip.cost
        fastResponseData['totalCost'] = str(totalCost) + ' ' + lastTrip.currency
        totalDuration = timedelta()
        for trip in trips:
            totalDuration += trip.duration
        fastDuration = totalDuration
        fastResponseData['totalDuration'] = str(totalDuration)
        fastResponseData['path']=serializer.data
        """
            Balanced path
        """
        trips = []
        toVisit = ['Paris', 'Londres', 'Barcelona']
        trip = Trip.objects.all(
            ).filter(fromPort__city=src
            ).filter(toPort__city__in=toVisit
            ).filter(departure__range=(startDate, startDate + timedelta(days=1))
            ).extra(select={'uglyness': "cost/10  + duration/60000000"}
            ).extra(order_by=['uglyness']
            )[0]
        trips.append(trip)
        toVisit.remove(trip.toPort.city)
        lastTrip = trip
        while len(toVisit) > 0:
            trip = Trip.objects.all(
                ).filter(fromPort__city=lastTrip.toPort.city
                ).filter(toPort__city__in=toVisit
                ).filter(departure__range=(lastTrip.arrival, startDate + timedelta(days=vacationDays-len(toVisit)))
                ).extra(select={'uglyness': "cost/10  + duration/60000000"}
                ).extra(order_by=['uglyness']
                )[0]
            trips.append(trip)
            toVisit.remove(trip.toPort.city)
            lastTrip = trip
        trip = Trip.objects.all(
            ).filter(fromPort__city=lastTrip.toPort.city
            ).filter(toPort__city=src
            ).filter(departure__gt=lastTrip.arrival
            ).filter(arrival__lt=startDate + timedelta(days=vacationDays)
            ).extra(select={'uglyness': "cost/10  + duration/60000000"}
            ).extra(order_by=['uglyness']
            )[0]
        trips.append(trip)
        responseData = {}
        serializer = TripSerializer(trips, many=True)
        totalCost = 0
        for trip in trips:
            totalCost += trip.cost
        balancedResponseData['totalCost'] = str(totalCost) + ' ' + lastTrip.currency
        totalDuration = timedelta()
        for trip in trips:
            totalDuration += trip.duration
        balancedResponseData['totalDuration'] = str(totalDuration)
        balancedResponseData['path']=serializer.data

        responseData['cheap'] = cheapResponseData
        responseData['fast'] = fastResponseData
        responseData['balanced'] = balancedResponseData
        return JsonResponse(responseData, safe=False)

    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)
