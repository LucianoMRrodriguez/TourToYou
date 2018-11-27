from datetime import timedelta
POSIBLE_FILTERS = ['Stay in city for at least', 'Scales', 'Duration']

def apply_filter(qSet, filtr, lastTrip, strategy, src, toVisit, startDate, vacationDays):
    if filtr != None and filtr['name'] == 'Stay in city for at least':
        if filtr['used']:
            return qSet
        if lastTrip.toPort.city == filtr['cityName']:
            qSet = qSet.filter(departure__gte=lastTrip.arrival + timedelta(days=int(filtr['daysToStay'])))
            filtr['used'] = True
        else:
            qSet = qSet.filter(arrival__lte=startDate + timedelta(days=vacationDays-int(filtr['daysToStay'])-len(toVisit)+1))
    
    if filtr != None and filtr['name'] == 'Scales':
        qSet = qSet.filter(scales__lte=int(filtr['max']))

    if filtr != None and filtr['name'] == 'Duration':
        qSet = qSet.filter(duration__lte=timedelta(seconds=int(filtr['max'])))
    
    if filtr != None and filtr['name'] == 'Connection':
        if filtr['used']:
            return qSet
        if (lastTrip != None and (lastTrip.toPort.city == filtr['fromPlace'] or lastTrip.toPort.name == filtr['fromPlace'])) or (src == filtr['fromPlace'] or src == filtr['fromPlace']):
            print('Applying connection')
            if filtr['toPort'] != None:
                print('port')
                qSet = qSet.filter(toPort__name=filtr['toPort'])
            if filtr['toCity'] != None:
                print('city')
                qSet = qSet.filter(toPort__city=filtr['toCity'])
            filtr['used'] = True
        else:
            print('Exclude')
            if filtr['toPort'] != None:
                print('port')
                qSet = qSet.exclude(toPort__name=filtr['toPort'])
            if filtr['toCity'] != None:
                print('city')
                qSet = qSet.exclude(toPort__city=filtr['toCity'])
        print('DONE')
    return qSet