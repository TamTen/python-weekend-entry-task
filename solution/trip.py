
import sys


class trip:
    def __init__(self, flights, number_of_bags):
        self.flights = flights
        self.bags_allowed = self.allowed_bags_count(flights)
        self.bags_count = number_of_bags
        self.destination = flights[-1].destination
        self.origin = flights[0].origin
        self.total_price = self.calculate_total_price(flights, self.bags_count)
        self.travel_time = flights[-1].arrival - flights[0].departure

    def calculate_total_price(self, flights, bags_count):
        total_price = 0
        for flight in flights:
            total_price += flight.base_price
            total_price += flight.bag_price * bags_count
        return total_price

    def allowed_bags_count(self, flights):
        max_bags = sys.maxsize
        for flight in flights:
            if(flight.bags_allowed < max_bags):
                max_bags = flight.bags_allowed
        return max_bags
