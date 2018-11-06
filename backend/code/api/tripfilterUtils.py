from datetime import timedelta
POSIBLE_FILTERS = ['Stay in city for at least']

def apply_filter(qSet, filtr, lastTrip, strategy, src, toVisit, startDate, vacationDays):
    if filtr['name'] == 'Stay in city for at least':
        print(lastTrip.toPort.city)
        if filtr['used']:
            return qSet
        if lastTrip.toPort.city == filtr['cityName']:
            qSet = qSet.filter(departure__gte=lastTrip.arrival + timedelta(days=filtr['daysToStay']))
            filtr['used'] = True
        else:
            qSet = qSet.filter(arrival__lte=startDate + timedelta(days=vacationDays-filtr['daysToStay']-len(toVisit)+1))
    return qSet