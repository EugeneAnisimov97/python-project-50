import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument("-f", '--FORMAT', help='set format of output')
    args = parser.parse_args()


if __name__ == '__main__':
    main()
