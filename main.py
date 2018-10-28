from Trip import Trip
from datetime import datetime,timedelta

trip = Trip('France', 'Paris', 'Orly', 'Netherlands', 'Amsterdam', 'Schiphol',
        3444, 'ARS', datetime(2018, 1, 2, 14, 0, 0),
        datetime(2018, 1, 3, 8, 30, 0), timedelta(hours=12,minutes=45), ['Nantes'])
