from datetime import timedelta
from trip import trip

MIN_WAIT_TIME = timedelta(hours=1)
MAX_WAIT_TIME = timedelta(hours=6)


def find_trips(airports, origin, destination, number_of_bags, return_trip):
    """
    Find all trips from origin to destination.

    Parameters
    ----------
    airports : dict
        Dictionary of all airports.
    origin : str
        Code of origin airport.
    destination : str
        Code of destination airport.
    number_of_bags : int
        Minimal number of bags that must be allowed for trip.
    return_trip : bool
        True if return trip should be included.

    Returns
    -------
    List
        List with all available paths.
    """

    if(not check_airport_presence(airports, origin)):
        print(f'No data for {origin} airport.')
        return
    if(not check_airport_presence(airports, destination)):
        print(f'No data for {destination} airport.')
        return

    paths = []
    find_paths(airports, origin, destination, paths)

    if (return_trip):
        return_paths = []
        find_paths(airports, destination, origin, return_paths)
        entire_paths = []
        for path in paths:
            for return_path in return_paths:
                entire_paths.append(path + return_path[1:])
        paths = entire_paths

    all_trips = []
    for path in paths:
        all_trips += find_trips_for_path(path, airports, number_of_bags)

    return [trip(_trip, number_of_bags) for _trip in all_trips]


def find_paths(airports, origin, destination, paths, visited=[]):
    """
    Searches for all available unique paths from origin to destination.

    Parameters
    ----------
    airports : dict
        Dictionary of all airports.
    origin : str
        Code of origin airport.
    destination : str
        Code of destination airport.
    paths : list
        List where valid paths will be stored.
    visited : list, optional
        List with already visited airports in path.
    """

    visited_airports = visited.copy()
    visited_airports.append(origin)

    for next_airport in airports[origin].destinations.keys():
        if(next_airport in visited_airports):
            continue
        if(next_airport == destination):
            path = visited_airports.copy()
            path.append(destination)
            paths.append(path)
            continue
        find_paths(airports, next_airport, destination,
                   paths, visited_airports)
    return


def find_trips_for_path(path, airports, number_of_bags):
    """
    Searches for all trips with a given path. Trip is a sequence of connecting
    flights from origin to destination.

    Parameters
    ----------
    path : list
        List of airports codes from origin to destination.
    airports : dict
        Dictionary of all airports.
    number_of_bags : int
        Minimal number of bags that must be allowed for each flight in the path.

    Returns
    -------
    List
        List with trips.
    """

    trips = []

    for i in range(0, len(path) - 1):
        trips = connect_airports(
            trips, airports, path[i], path[i+1], number_of_bags)
        if (len(trips) == 0):
            return []
    return trips


def connect_airports(trips, airports, from_airport, to_airport, number_of_bags):
    """
    Searches for connecting flights between two airports that are connected to previous
    flights and can transport a given number of bags.

    Parameters
    ----------
    trips : list
        Previous flights in a trip.
    airports : dict
        Dictionary of all airports.
    from_airport : str
        Start of flight.
    to_airport : str
        End of flight.
    number_of_bags : int
        Minimal number of bags that must be allowed for each flight.

    Returns
    -------
    List
        Updated list with trips.
    """

    new_trips = []

    if(len(trips) == 0):
        flights = airports[from_airport].destinations[to_airport][1]
        for flight in flights:
            if(flight.bags_allowed >= number_of_bags):
                new_trips.append([flight])
        return new_trips

    for trip in trips:
        flights = airports[from_airport].destinations[to_airport][1]
        for flight in flights:
            if(flight.departure > trip[-1].arrival
                    and MIN_WAIT_TIME < flight.departure - trip[-1].arrival < MAX_WAIT_TIME
                    and flight.bags_allowed >= number_of_bags):
                new_trip = trip.copy()
                new_trip.append(flight)
                new_trips.append(new_trip)
    return new_trips


def check_airport_presence(airports, airport):
    """
    Check if airport is presented in dictionary of airports.

    Parameters
    ----------
    airports : dict
        Dictionary of all airports.
    airport : str
        Airport code.

    Returns
    -------
    bool
        True if airport is in airports.
    """

    return airport in airports.keys()
