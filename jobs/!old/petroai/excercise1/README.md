## Exercise 1: Linear regression analysis

- If you don't already have Python installed, [install python 3.9 or greater](https://www.python.org/downloads/)
- Either create a new virtual environment inside the project or use your existing python interpreter
- In a terminal

      pip install pipenv
      pipenv install

## Choices

- Used 2014 and 2015 data as test set. Did not retrain model with 2014 data to predict 2015 data
- Converted status and country to numerical data
- Used r<sup>2</sup> as scoring metric as it seemed reasonable. Didn't check any other metrics

## How to Run

## Excercise 1

In a terminal ```python excercise1/excercise1.py```. This prints out a table containing the decisions made in prepping
the data, the model, and the score. The model with the best score is saved to `excercise1/classifier.pkl` along with the
best dataset to `excercise1/final_dataset.csv`

### Model Performance

The best model had the following parameters

- use population column = False
- use country number column = False
- replaced null values in the input data with the mean of the country's values
- model = sklearn.LinearRegression()
- r2 score = 0.808604 predicting 2014 and 2015 life expectancy

- Table of all experiment results

          use_population  use_country_number    replace_nulls_with               model        r2
      9            False               False                  mean  LinearRegression()  0.808604
      3             True               False                  mean  LinearRegression()  0.808535
      6            False                True                  mean  LinearRegression()  0.808043
      0             True                True                  mean  LinearRegression()  0.807978
      10           False               False                median  LinearRegression()  0.807772
      4             True               False                median  LinearRegression()  0.807724
      7            False                True                median  LinearRegression()  0.807386
      1             True                True                median  LinearRegression()  0.807335
      11           False               False  linear interpolation  LinearRegression()  0.804935
      5             True               False  linear interpolation  LinearRegression()  0.804852
      8            False                True  linear interpolation  LinearRegression()  0.803984
      2             True                True  linear interpolation  LinearRegression()  0.803901

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

### Notes I took while working on problem

- It's possible that the entire column can be null. In this case, we need to fill NA values with mean of the entire
  column

- Could look up the additional statistics, would probably be a good idea For example, the population is knowable yeah?
  Find table with country and population for that year. Checking the correlation of population with life expectancy is
  only 0.02 correlation with life. Going to just try dropping it then

      print(df.corr()[life_exp_col].abs().sort_values())

      CountryNumber                      0.016763
      Population                         0.021538
      Measles                            0.157586
      Year                               0.170033
      infant deaths                      0.196557
      Total expenditure                  0.218086
      under-five deaths                  0.222529
      Hepatitis B                        0.256762
      percentage expenditure             0.381864
      Alcohol                            0.404877
      GDP                                0.461455
      Polio                              0.465556
       thinness 5-9 years                0.471584
       thinness  1-19 years              0.477183
      Diphtheria                         0.479495
      Status                             0.482136
       HIV/AIDS                          0.556556
       BMI                               0.567694
      Adult Mortality                    0.696359
      Income composition of resources    0.724776
      Schooling                          0.751975
      Life expectancy                    1.000000
      Name: Life expectancy , dtype: float64

- Tried dropping all rows with null values but that removes 44% of the data, so not a viable option

      (2938 - 1649) / 2938 * 100 = 43.9