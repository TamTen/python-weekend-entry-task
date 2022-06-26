import argparse
from xmlrpc.client import boolean


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Python script for flight data processing.')
    parser.add_argument('file_name', type=str, nargs=1,
                        help='.csv file with data.')
    parser.add_argument('origin', type=str, nargs=1,
                        help='Origin airport of the trip.')
    parser.add_argument('destination', type=str, nargs=1,
                        help='The final destination of the trip.')
    parser.add_argument('-b', '--bags', metavar='N', type=int, nargs='?', default=0,
                        help='Number of bags for trip.')
    parser.add_argument('--return', action='store_true',
                        help='Include return trip.')
    args = vars(parser.parse_args())

    return args
