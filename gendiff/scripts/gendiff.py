#!/usr/bin/env python3
from gendiff.cli import parse_arguments
from gendiff.generate_diff import generate_diff


def main():
    arguments = parse_arguments()
    diff = generate_diff(arguments.first_file, arguments.second_file, arguments.FORMAT)  # noqa: E501
    return diff


if __name__ == '__main__':
    main()
