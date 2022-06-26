import csv
from airport import Airport
from flight import Flight


def parse_file(file_name):
    """
    Parse .csv file with flights. Expected header is 
    flight_no,origin,destination,departure,arrival,base_price,bag_price,bags_allowed

    Parameters
    ----------
    file_name : str
        .csv file with flights.

    Returns
    -------
    Dictionary
        Dictionary with airports.
    """

    airports = {}
    try:
        with open(file_name, newline='') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            for row in reader:
                if(not row['origin'] in airports.keys()):
                    airports[row['origin']] = Airport(row['origin'])
                if(not row['destination'] in airports.keys()):
                    airports[row['destination']] = Airport(row['destination'])
                if(not airports[row['origin']].is_destination(row['destination'])):
                    airports[row['origin']].add_destination(
                        airports[row['destination']])

                flight = Flight(flight_number=row['flight_no'], origin=row['origin'],
                                destination=row['destination'], departure=row['departure'],
                                arrival=row['arrival'], base_price=row['base_price'],
                                bag_price=row['bag_price'], bags_allowed=row['bags_allowed'])

                airports[row['origin']].add_flight_to_destination(
                    airports[row['destination']], flight)

    except FileNotFoundError:
        print(f'File {file_name} not found.')
        return None
    except KeyError:
        print(f'Wrong data or data header.')
        print(f'Expected header: flight_no,origin,destination,departure,arrival,base_price,bag_price,bags_allowed.')
        return None
    except ValueError:
        print(f'Unexpected data type in file.')
        return None
    except Exception as e:
        print(f'Unexpected problem associated to file: {e}')
        return None

    return airports
