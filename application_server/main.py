#! /usr/bin/python3.6
# -*- coding: utf-8 -*-

"""
    Scans the DSLS Administration folder logs and prints the results to the console screen.

    config_.json must exist in the same folder and have values for log_file_directory and max_files.
    log_file_directory is the path to the folder containing the log files.
    max_files is the maximum number of log files the script will scan.

    The DSLS Administrator tool must be configured to log license usage. To do this double click on the server
    you wish to log select the button "License usage tracking" and check the licenses you wish to track.

"""

from datetime import datetime
import json
from operator import itemgetter
import os


def create_json():
    """
    Creates the file config.json.
    :return:
    """
    folder_path = input("Please enter path to log files: ")
    max_files = input("Please enter maximum number of config files to parse: ")
    data = {
        "log_file_directory": folder_path,
        "max_files": int(max_files)
    }
    with open('config.json', 'w') as f:
        json.dump(data, f)


def log_entry_parser(entry_):
    """
    Parses the line with license usage text information and returns a dictionary containing
    data required.
    :param entry_:
    :return: dict()
    """
    entry = dict()

    entry['date'] = datetime.strptime(entry_[0:23], '%Y/%m/%d %H:%M:%S:%f')

    split_entry = entry_[38:].split('!')
    entry['status'] = split_entry[0]
    entry['license'] = split_entry[2]
    entry['user'] = split_entry[10]
    entry['machine'] = split_entry[8]

    return entry


def read_log_file(log_file, log_lines, search=None):
    """

    :param log_file: text log file
    :param log_lines: list()
    :param search: string()
    :return:
    """
    with open(log_file, 'r', errors='ignore') as f:
        for line in f:
            if 'USGTRACING' in line:
                if search:
                    if search.lower() in line.lower():
                        log_lines.append(log_entry_parser(line.strip()))
                else:
                    log_lines.append(log_entry_parser(line.strip()))
    return log_lines


def pretty_print_log_data(log_data):
    """

    :param log_data:
    :return:
    """
    for entry in log_data:
        print('Date: {} | License: {} | User: {} | Status: {} | Machine: {}'.format(entry['date'],
                                                                                    entry['license'].ljust(10),
                                                                                    entry['user'].ljust(20),
                                                                                    entry['status'].ljust(10),
                                                                                    entry['machine']))


def main(config_file, search=None):
    """
    :param config_file: config.json
    :param search: string()
    :return:
    """

    if not os.path.isfile(config_file):
        print('Could not find config.json file. Would you like to create that now?')
        create_json()
        print('Please run script again.')
        exit()

    with open(config_file) as f:
        json_data = json.load(f)

    # had instances where max_files wasn't set. no clue why, problem was intermittent.
    if 'max_files' not in json_data:
        json_data['max_files'] = 1

    log_data = list()
    max_files = json_data['max_files']
    i = 0
    for root, dir, files in os.walk(json_data['log_file_directory']):
        files = [fi for fi in files if fi.endswith(".log")]
        for file in sorted(files, reverse=True):
            log_data = read_log_file(os.path.join(root, file), log_data, search)
            if i == max_files:
                break
            i += 1
        if i == max_files:
            break

    # sort the log_data by datetime in reverse
    log_data.sort(key=itemgetter('date'), reverse=True)

    return log_data


if __name__ == "__main__":
    config_file = 'config.json'
    result = main(config_file)
    pretty_print_log_data(result)
