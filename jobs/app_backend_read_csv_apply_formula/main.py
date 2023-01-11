import argparse

from power_calc import run_main

parser = argparse.ArgumentParser(
    description='Input a json file of objects with voltage, current, and PF (PF is optional), calculate and return an'
                ' object containing apparent, real and reactive power')
parser.add_argument("--filename", help='Name of json file')
args = parser.parse_args()
if not args.filename:
    raise ValueError('--filename argument was not specified')
data = run_main(args.filename)
for k, v in data.items():
    print(k, v)
