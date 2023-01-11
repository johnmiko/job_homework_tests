import itertools
import warnings
import os
from pathlib import Path

import joblib
import pandas as pd
from sklearn import linear_model
from sklearn.metrics import r2_score
from sklearn.preprocessing import LabelEncoder

# Lots of FutureWarning errors, choosing to suppress as this is a homework assignment
warnings.filterwarnings("ignore")

# Get the excercise1 directory so that the file can be run from either the root directory or this folder
exc_1_dir = os.path.dirname(os.path.abspath(Path(__file__)))
filename = f"{exc_1_dir}/Life Expectancy Data.csv"
classifier_file = f"{exc_1_dir}/classifier.pkl"
final_dataset_file = f"{exc_1_dir}/final_dataset.csv"
life_exp_col = "Life expectancy "  # create variable as original name has a space at the end
df_raw = pd.read_csv(filename)
df = df_raw.copy()
label_encoder = LabelEncoder()
# Convert category "developing/developed" to numerical
# df['Status'] = df['Status'].replace('Developing', 0).replace('Developed', 1) # can do manually as another option
df['Status'] = label_encoder.fit_transform(df['Status'])
df['CountryNumber'] = label_encoder.fit_transform(df['Country'])


def replace_nulls_with(df, method_name):
    """
    :param method_name: Formula to replace null values with (mean, median, linear interpolation)
    :param df: Dataframe
    :return: Dataframe with single null values replaced by method_name. Entire null columns are replaced with the mean or median
    """
    group = df.groupby('Country')
    if method_name == 'mean':
        df2 = group.transform('mean')
        df3 = df.fillna(df2)
        df4 = df3.fillna(df.mean(numeric_only=True))
    elif method_name == 'median':
        df2 = group.transform('median')
        df3 = df.fillna(df2)
        df4 = df3.fillna(df.median(numeric_only=True))
    elif method_name == 'linear interpolation':
        df2 = group.apply(lambda group: group.interpolate(method='index'))
        df3 = df.fillna(df2)
        df4 = df3.fillna(df.median(numeric_only=True))
    else:
        raise ValueError(f'{method_name} not a valid strategy for replacing nulls')
    return df4


def drop_columns(df, row):
    if not row['use_population']:
        df = df.drop(['Population'], axis=1)
    if not row['use_country_number']:
        df = df.drop(['CountryNumber'], axis=1)
    df = df.drop(['Country'], axis=1)
    return df


drop_population = [True, False]
drop_country_number = [True, False]
replace_nulls = ['mean', 'median', 'linear interpolation']
# Prepare data with all possible choices to see if they make a difference or not
combinations = list(itertools.product(drop_population, drop_country_number, replace_nulls))
df_result = pd.DataFrame(combinations, columns=['use_population', 'use_country_number', 'replace_nulls_with'])

for i, row in df_result.iterrows():
    df2 = replace_nulls_with(df, row['replace_nulls_with'])
    df_use = drop_columns(df2, row)
    mask = (df_use['Year'] == 2015) | (df_use['Year'] == 2014)
    df_train = df_use[~mask]
    X_train = df_train.drop(life_exp_col, axis=1)
    y_train = df_train[life_exp_col]
    df_test = df_use[mask]
    X_test = df_test.drop(life_exp_col, axis=1)
    y_test = df_test[life_exp_col]

    # Scaling not necessary since we are doing Linear Regression
    clf = linear_model.LinearRegression()

    clf.fit(X_train, y_train)
    df_result.at[i, 'model'] = clf
    df_train = df_use
    # r2 score: 0% represents a model that does not explain any of the variation in the response variable around its
    # mean. The mean of the dependent variable predicts the dependent variable as well as the regression model. 100%
    # represents a model that explains all the variation in the response variable around its mean.
    df_result.at[i, 'r2'] = r2_score(y_test, clf.predict(X_test))

# Print to the screen the r2 score and variables used in the calculation
print('Possible choices for preparing the data along with model used and r2 score')
df_result = df_result.sort_values('r2', ascending=False)
print(df_result.to_string())
# Fit classifier using all of the data and pickle result to file
row = df_result.iloc[0]
df2 = replace_nulls_with(df, row['replace_nulls_with'])
df_use = drop_columns(df2, row)
df_use.to_csv(final_dataset_file, index=False, header=True)
df_train = df_use
X_train = df_train.drop(life_exp_col, axis=1)
y_train = df_train[life_exp_col]
clf = linear_model.LinearRegression()
clf.fit(X_train, y_train)
_ = joblib.dump(clf, classifier_file)
print(f'Saved classifier to {classifier_file} and final dataset to {final_dataset_file}')
