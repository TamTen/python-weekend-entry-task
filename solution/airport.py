
class Airport:
    def __init__(self, airport_code):
        self.code = str(airport_code)
        self.destinations = {}

    def is_destination(self, destination_code):
        return destination_code in self.destinations.keys()

    def add_destination(self, destination):
        self.destinations[destination.code] = (destination, [])

    def add_flight_to_destination(self, destination, flight):
        self.destinations[destination.code][1].append(flight)
