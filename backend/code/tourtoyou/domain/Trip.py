from Port import *
from Price import *
from datetime import datetime,timedelta

class Trip:
    
    def __init__(self, fromCountry, fromCity, fromPort,
    toCountry,toCity,toPort, costValue, costCurrency,
    departureDatetime, arrivalDatetime, totalTimedelta, scales):
        self.fromPort = Port(fromCountry, fromCity, fromPort)
        self.toPort = Port(toCountry, toCity, toPort)
        self.cost = Price(costValue, costCurrency)
        self.departure = departureDatetime
        self.arrival = arrivalDatetime
        self.totalTime = totalTimedelta
        self.scales = scales

         

    