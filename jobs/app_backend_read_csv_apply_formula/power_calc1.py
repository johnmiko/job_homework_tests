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
# 7.) Program outputs the n ew dictionary in a user readable manner.

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
ACCEPTABLE_KEY_VALUES = I_NAMES + PF_NAMES + V_NAMES


def calc_power(volts, amps, pf=0.9):
    #   Note: Some of the input data doesn’t include power factor. In those cases, please assume a power factor of 0.9.
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
    # 4.) Program creates a new dictionary that has the same location as the primary key, but the value is three new
    #       calculated quantities:
    #           s = apparent power
    #           p = real power
    #           q = reactive power
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


def update_dict_key_if_found(data, key2, key1, names):
    if key2 in names:
        data[key1][names[0]] = data[key1].pop(key2)
    return data


def clean_json_data(data):
    # 3.) Program can clean json file:
    #   a) ensure it is semantically correct and have known quantities for voltage, current, and power factor.
    #   b) Use allowable names (V_NAMES, I_NAMES, PF_NAMES) provided below to clean keys.
    # Assume that data is always a dictionary of dictionaries
    for k1, v1 in data.items():
        for k2, v2 in v1.items():
            # TODO: something like this
            # for names in (I_NAMES, PF_NAMES, V_NAMES):
            # data = update_dict_key_if_found(data, k2, k1, I_NAMES)
            # key_found = False
            # if k2 in names:
            #     key_found = True
            #     data[k1][names[0]] = data[k1].pop(k2)
            #     break
            if k2 in I_NAMES:
                data[k1][I_NAMES[0]] = data[k1].pop(k2)
            elif k2 in PF_NAMES:
                data[k1][PF_NAMES[0]] = data[k1].pop(k2)
            elif k2 in V_NAMES:
                data[k1][V_NAMES[0]] = data[k1].pop(k2)
            else:
                # if not key_found:
                raise ValueError(
                    f'Data has a key of "{k2}".\n\tKey must be one of {ACCEPTABLE_KEY_VALUES}')
            # Not 100% clear in question 3a what "ensure it is semantically correct and have known quantities for
            # voltage, current, and pwer factor." means. Going to assume this means value must be a number
            if not isinstance(v2, numbers.Number):
                raise ValueError(
                    f'Data has a value of "{v2}" which is type {type(v2)}. Value must be a valid number')
        if not v1:
            raise ValueError(
                f'Data has a value of "{v1}". Expected a dictionary of power type and value pairs')
    return data


# 3.) Program can clean json file:
#   a) ensure it is semantically correct and have known quantities for voltage, current, and power factor.
#   b) Use allowable names (V_NAMES, I_NAMES, PF_NAMES) provided below to clean keys.

def run(filename):
    data = get_data_from_file(filename)
    data2 = clean_json_data(data)
    for key, value in data2.items():
        pf = value.get('pf', 0.9)
        volts = value['v']
        amps = value['i']
        data2[key] = calc_power(volts, amps, pf=pf)
    return data2
    # 5.) Use the "calc_power" function to handle the calculations for the new dictionary.
    #   Note: Some of the input data doesn’t include power factor. In those cases, please assume a power factor of 0.9.
    # 6.) Complete the TODO in calc_power. Use the calc_power doc string for more information.
    # 7.) Program outputs the n ew dictionary in a user readable manner.


# Run the program; expects a single argument which is the name of JSON file
if __name__ == "__main__":
    # 1.) Program can accept a json file (ie. data1.json) from the command line.
    filename = sys.argv[1]
    data = run(filename)
    for k, v in data.items():
        print(k, v)
# python power_calc.py data1.json
