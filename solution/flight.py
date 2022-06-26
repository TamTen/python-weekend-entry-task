from datetime import datetime


class Flight:
    def __init__(self, flight_number, origin, destination, departure, arrival, base_price, bag_price, bags_allowed):
        self.flight_number = str(flight_number)
        self.origin = str(origin)
        self.destination = str(destination)
        self.departure = datetime.fromisoformat(departure)
        self.arrival = datetime.fromisoformat(arrival)
        self.base_price = float(base_price)
        self.bag_price = float(bag_price)
        self.bags_allowed = int(bags_allowed)
