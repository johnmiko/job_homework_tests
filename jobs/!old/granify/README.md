# Requirements

* If you don't already have Python installed, [install python 3.6 or greater](https://www.python.org/downloads/)
* Either create a new virtual environment inside the project or use your existing python interpreter
* I didn't use any additional libraries, the default python libraries are enough

# Miscellaneous

In python, the convention is to name objects with lower snake case (lower_snake_case), used lower camel case
(lowerCamelCase) to match the assignment more closely

# How to Run

## Part 1

- In a terminal
- ```python part_1/main.py```
- Note: In assignment it says to verify the output is

```
Name is currently
Name has been changed to Garfield
Inserting Garfield into table Cat
```

This is missing the line `connecting to database` which is printed when the Data object is initialized. The correct
output should be

```
Name is currently
Name has been changed to Garfield
Connecting to database
Inserting Garfield into table Cat
```

Also, in Python, you can print the value "None" to the screen, so just converting the pseudo code to Python, the first
line says "Name is currently None". In a case like this, do you want me to edit the code so the word "None" is not
printed or not?

## Part 2

- View the code in the directory `part_2` to see the code changes requested in the assignment
- Note: In Part 5, it's not 100% clear when a cat is created without a name, if this "unnamed" period should be added to
  the list of names. Chose to not record anything if the cat was initially not named as it seemed it may mess with the
  expected result of part 2.8 getAverageNameLength()

## Part 3

- In a terminal
- ```python part_3/petShop.py```
- See in the console the print statements when interacting with a mock database and performance logs from cProfile

## SQL Tasks

View sample SQL statements in the file `homework.sql`

## Testing Tasks

View tests in `tests.py`
Run the tests with `python -m unittest tests.py`
