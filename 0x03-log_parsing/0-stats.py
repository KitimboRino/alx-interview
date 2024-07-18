#!/usr/bin/python3

import sys

def print_msg(dict_sc, total_file_size):
    """
    Method to print
    Args:
        dict_sc: dict of status codes
        total_file_size: total of the file
    Returns:
        Nothing
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))

total_file_size = 0
counter = 0
dict_sc = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 10:
            continue

        ip = parts[0]
        date = parts[3][1:]
        request = parts[5][1:]
        path = parts[6]
        protocol = parts[7][:-1]
        status_code = parts[8]
        file_size = parts[9]

        if request != 'GET' or path != '/projects/260' or protocol != 'HTTP/1.1':
            continue

        try:
            file_size = int(file_size)
            total_file_size += file_size
        except ValueError:
            continue

        if status_code in dict_sc:
            dict_sc[status_code] += 1

        counter += 1
        if counter == 10:
            print_msg(dict_sc, total_file_size)
            counter = 0

except KeyboardInterrupt:
    print_msg(dict_sc, total_file_size)
    sys.exit(0)

# Final statistics print in case the input ends before 10 lines are processed
print_msg(dict_sc, total_file_size)
