import json


def create_json(trips):
    trips = sorted(trips, key=lambda flight: flight.total_price)
    return json.dumps(
        [
            {'flights': [{'flight_no': flight.flight_number,
                          'origin': flight.origin,
                          'destination': flight.destination,
                          'departure': str(flight.departure.isoformat()),
                          'arrival': str(flight.arrival.isoformat()),
                          'base_price': flight.base_price,
                          'bag_price': flight.bag_price,
                          'bags_allowed': flight.bags_allowed
                          } for flight in trip.flights],
             'bags_allowed': trip.bags_allowed,
             'bags_count': trip.bags_count,
             'destination': trip.destination,
             'origin': trip.origin,
             'total_price': trip.total_price,
             'travel_time': str(trip.travel_time)
             } for trip in trips
        ], indent=4)
