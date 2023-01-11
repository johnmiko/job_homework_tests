#!/usr/bin/python
#
# Instructions & Requirements
# ---------------------------
# Complete the code to fulfill the below Acceptance Criteria.

# Acceptance Criteria
# -------------
# 1.) Program can accept a json file (ie. data1.json) from the command line.
# 2.) Program can verify that json file exists and is in expected format.
# 3.) Program can clean json file:
#   a) ensure it is semantically correct and have known quantities for voltage, current, and power factor.
#   b) Use allowable names (V_NAMES, I_NAMES, PF_NAMES) provided below to clean keys.
# 4.) Program creates a new dictionary that has the same location as the primary key, but the value is three new
#       calculated quantities:
#           s = apparent power
#           p = real power
#           q = reactive power
# 5.) Use the "calc_power" function to handle the calculations for the new dictionary.
#   Note: Some of the input data doesn’t include power factor. In those cases, please assume a power factor of 0.9.
# 6.) Complete the TODO in calc_power. Use the calc_power doc string for more information.
# 7.) Program outputs the ew dictionary in a user readable manner.

# Notes
# -----
# Treat this code as if you were going to put this into production. We want to see how you would code with us.
# Write the code so that it is testable and show some examples of unit tests (full coverage not expected).
# Make the code robust (e.g. Error handling, managing unexpected input, etc)
# Make the code readable. Remember, comments aren't the only way to make code readable.
# Make the code clean. Don't be afraid to clean up code that is already written.
# Make the code reusable. It's not easy to reuse a main function.
# Don't spend more than an hour on this.
# If there are refactorings or improvements that you would do if you had more time, make notes of that.
import json
import math
import numbers
import sys

# Allowable names for voltage, current, and power factor
V_NAMES = ('v', 'V', 'Volts', 'Voltage')
I_NAMES = ('i', 'I', 'Amps', 'Amperes', 'Current')
PF_NAMES = ('pf', 'PF', 'Power Factor')
ACCEPTABLE_KEY_VALUES = V_NAMES + I_NAMES + PF_NAMES


def calc_power(volts, amps, pf):
    #   Note: Some of the input data doesn’t include power factor. In those cases, please assume a power factor of 0.9.
    # 4.) Program creates a new dictionary that has the same location as the primary key, but the value is three new
    #       calculated quantities:
    #           s = apparent power
    #           p = real power
    #           q = reactive power
    # 5.) Use the "calc_power" function to handle the calculations for the new dictionary.
    #   Note: Some of the input data doesn’t include power factor. In those cases, please assume a power factor of 0.9.
    # 6.) Complete the TODO in calc_power. Use the calc_power doc string for more information.
    '''Returns tuple of (p, q, s) powers from the inputs.

        Note that the relationship between p, q, and s can be described with a right triangle.
            \
            | \
            |   \
          q |     \  s
            |       \
            |_        \
            |_|_________\
                 p
    '''
    try:
        s = round(volts * amps, 2)
        p = round(s * pf, 2)
        q = round(math.sqrt(s ** 2 - p ** 2), 2)
        return p, q, s
    except (ValueError, TypeError):
        return None, None, None


def get_data_from_file(filename):
    try:
        # 2.) Program can verify that json file exists and is in expected format.
        # Python convention is "it's better to ask for forgiveness than permission. So use try/except to read file
        # If we needed to explicitly check that the file exists first, we could instea do
        # import os.path
        # os.path.isfile(filename)
        with open(filename) as f:
            return json.loads(f.read())
    except FileNotFoundError:
        # Could just do "raise e" here. Writing custom message to match acceptance criteria
        raise FileNotFoundError(f'file "{filename}" does not exist')


def update_key_name(data, k1, k2):
    # 3a) ensure it is semantically correct and have known quantities for voltage, current, and power factor.
    key_found = False
    for names in (V_NAMES, I_NAMES, PF_NAMES):
        if k2 in names:
            data[k1][names[0]] = data[k1].pop(k2)
            key_found = True
            break
    if not key_found:
        #   a) ensure it is semantically correct and have known quantities for voltage, current, and power factor.
        #   b) Use allowable names (V_NAMES, I_NAMES, PF_NAMES) provided below to clean keys.
        raise ValueError(
            f'Data has a key of "{k2}".\n\tKey must be one of {ACCEPTABLE_KEY_VALUES}')
    return data


def clean_json_data(data):
    # 3.) Program can clean json file:
    #   a) ensure it is semantically correct and have known quantities for voltage, current, and power factor.
    #   b) Use allowable names (V_NAMES, I_NAMES, PF_NAMES) provided below to clean keys.
    # Assume that data is always a dictionary of dictionaries
    for k1, v1 in data.items():
        for k2, v2 in v1.items():
            data = update_key_name(data, k1, k2)
            if not isinstance(v2, numbers.Number):
                raise ValueError(
                    f'Data has a value of "{v2}" which is type {type(v2)}. Value must be a valid number')
        if 'v' not in v1:
            raise ValueError(f'"{k1}" is missing a voltage value')
        elif 'i' not in v1:
            raise ValueError(f'"{k1}" is missing an amperes value')
    return data


def run_main(filename):
    data = get_data_from_file(filename)
    data2 = clean_json_data(data)
    for key, value in data2.items():
        # 5.) Use the "calc_power" function to handle the calculations for the new dictionary.
        #   Note: Some of the input data doesn’t include power factor. In those cases, please assume a power factor of 0.9.
        pf = value.get('pf', 0.9)
        volts = value['v']
        amps = value['i']
        data2[key] = calc_power(volts, amps, pf)
    return data2
    # 5.) Use the "calc_power" function to handle the calculations for the new dictionary.
    #   Note: Some of the input data doesn’t include power factor. In those cases, please assume a power factor of 0.9.
    # 6.) Complete the TODO in calc_power. Use the calc_power doc string for more information.
    # 7.) Program outputs the n ew dictionary in a user readable manner.


# Run the program; expects a single argument which is the name of JSON file
if __name__ == "__main__":
    # 1.) Program can accept a json file (ie. data1.json) from the command line.
    try:
        filename = sys.argv[1]
    except IndexError as e:
        raise IndexError('The json filename is missing')
    data = run_main(filename)
    # 7.) Program outputs the ew dictionary in a user readable manner.
    for k, v in data.items():
        print(k, v)
