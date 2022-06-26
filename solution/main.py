import argument_parser
import file_parser
import trip_finder
import json_builder

if __name__ == '__main__':
    airports = None
    trips = None
    result = None
    arguments = argument_parser.parse_arguments()

    if(arguments):
        airports = file_parser.parse_file(arguments['file_name'][0])
    if(airports):
        trips = trip_finder.find_trips(
            airports, arguments['origin'][0].upper(), arguments['destination'][0].upper(), arguments['bags'], arguments['return'])
    if(trips):
        result = json_builder.create_json(trips)
    if(result):
        print(result)
