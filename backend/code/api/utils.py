from api.models import Port, Trip
from api.serializers import PortSerializer, TripSerializer
from datetime import datetime, timedelta
import logging
from django.db.models import Q
from api.tripfilterUtils import apply_filter

CHEAP_STR = 'cheap'
FAST_STR = 'fast'
BALANCED_STR = 'balanced'
POSIBLE_STRATEGIES= [CHEAP_STR, FAST_STR, BALANCED_STR]

def calculate_path(strategy, src, toVisitCities, startDate, vacationDays, filters):
    data = {}
    if strategy not in POSIBLE_STRATEGIES:
        data['error'] = 'Bad request'
        return  data
    print(strategy)
    trips = []
    toVisit = toVisitCities[:]
    for f in filters['oncity']:
        f['used'] = False
    for f in filters['ontrip']:
        f['used'] = False
    try:
        """ Leaving home """
        tripQset = Trip.objects.all(
            ).filter(Q(fromPort__city=src) | Q(fromPort__name=src)
            ).filter(Q(toPort__city__in=toVisit) | Q(toPort__name__in=toVisit)
            ).filter(departure__range=(startDate, startDate + timedelta(days=1)))
        if filters != None:
            for f in filters['global']:
                tripQset = apply_filter(tripQset, f, None, strategy, src, toVisit, startDate, vacationDays)
            for f in filters['ontrip']:
                tripQset = apply_filter(tripQset, f, None, strategy, src, toVisit, startDate, vacationDays)
        trip = _getOrderBy(tripQset, strategy)
        trips.append(trip)
        if trip.toPort.city in toVisit: toVisit.remove(trip.toPort.city)
        if trip.toPort.name in toVisit: toVisit.remove(trip.toPort.name)
        lastTrip = trip
        print(lastTrip.fromPort.city)
        print(lastTrip.toPort.city)
        """ Visiting """
        while len(toVisit) > 0:
            tripQset = Trip.objects.all(
                ).filter(fromPort__city=lastTrip.toPort.city
                ).filter(Q(toPort__city__in=toVisit) | Q(toPort__name__in=toVisit)
                ).filter(departure__gte=lastTrip.arrival
                ).filter(arrival__lte=startDate + timedelta(days=vacationDays-len(toVisit)))
            if filters != None:
                for f in filters['oncity']:
                    tripQset = apply_filter(tripQset, f, lastTrip, strategy, src, toVisit, startDate, vacationDays)
                for f in filters['global']:
                    tripQset = apply_filter(tripQset, f, lastTrip, strategy, src, toVisit, startDate, vacationDays)
                for f in filters['ontrip']:
                    tripQset = apply_filter(tripQset, f, lastTrip, strategy, src, toVisit, startDate, vacationDays)
            trip = _getOrderBy(tripQset, strategy)
            trips.append(trip)
            if trip.toPort.city in toVisit: toVisit.remove(trip.toPort.city)
            if trip.toPort.name in toVisit: toVisit.remove(trip.toPort.name)
            lastTrip = trip
            print(lastTrip.fromPort.city)
            print(lastTrip.toPort.city)
        """ Going back home """
        tripQset = Trip.objects.all(
            ).filter(fromPort__city=lastTrip.toPort.city
            ).filter(Q(toPort__city=src) | Q(toPort__name=src) 
            ).filter(departure__gt=lastTrip.arrival
            ).filter(arrival__lt=startDate + timedelta(days=vacationDays))
        if filters != None:
            for f in filters['global']:
                tripQset = apply_filter(tripQset, f, lastTrip, strategy, src, toVisit, startDate, vacationDays)
            for f in filters['ontrip']:
                tripQset = apply_filter(tripQset, f, None, strategy, src, toVisit, startDate, vacationDays)
        trip = _getOrderBy(tripQset, strategy)
        trips.append(trip)
        print(lastTrip.fromPort.city)
        print(lastTrip.toPort.city)
        """ Final calculations """
        serializer = TripSerializer(trips, many=True)
        totalCost = 0
        for trip in trips:
            totalCost += trip.cost
        data['totalCost'] = str(totalCost) + ' ' + lastTrip.currency
        totalDuration = timedelta()
        for trip in trips:
            totalDuration += trip.duration
        data['totalDuration'] = str(totalDuration)
        data['path']=serializer.data
    except Exception as err:
        print(err)
        data['error'] = 'Path not found'
        pass
    return data

def _getOrderBy(qSet, strategy):
    if strategy == CHEAP_STR:
        trip = qSet.order_by('cost','duration')[0]
    elif strategy == FAST_STR:
        trip = qSet.order_by('duration','cost')[0]
    else:
        trip = qSet.extra(select={'uglyness': "cost/10  + duration/60000000"}
                ).extra(order_by=['uglyness'])[0]
    return trip