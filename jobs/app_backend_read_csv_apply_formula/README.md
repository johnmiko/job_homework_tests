# Software Developer Technical Test - John Miko

## Notes/Decisions

1. Renamed `power-calc` to `power_calc` so I could import from it
   <br><br>
2. Didn't specify in the requirements to check that Power Factor was a value between 0-1, so I did not check for it
3. Question 1) Program can accept a json file (ie. data1.json) from the command line.
   <br><br>
    - Since in `power_calc.py`, there is the line `if __name__ == "__main__":`, I allowed `power_calc.py` to be run
      directly. If this were production code, I think creating a file `main.py` and use
      `argparse` would be a bit better. I included `main.py` as well so you can see what it would look like.
      <br><br>
4. Question 3a) ensure it is semantically correct and have known quantities for voltage, current, and power factor
   <br><br>
    - Not 100% clear to me what *known quantities* means. Interpreted this to be that each value must be a valid number

## How to Run

In a terminal

`python power_calc.py data1.json`

or

`python main.py --filename=data1.json`

To view help type

`python main.py --help`

# Improvements/TODO

- In the tests, need to check that the exception message is correct
- Add tests for all functions and 100% code coverage for each function
- For allowable key names, compare lowercase values to allow for case-insensitivity
- We may want to have a separate error message for when both voltage and amps are missing
- Could improve print out of final values by converting to a pandas dataframe, or returning a dictionary instead of a
  tuple with names included to be a bit more clear
- May be beneficial in function `calc_power` to have pf have a default value of 0.9
- Could split the function `update_key_name` into 2 functions
- Probably want to check that if Power Factor is supplied, that the value is between 0 and 1