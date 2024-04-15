import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", '--FORMAT', help='set format of output', default='stylish', type=str)
    return parser.parse_args()
