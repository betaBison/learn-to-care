########################################################################
# Author(s):    D. Knowles
# Date:         26 Jul 2021
# Desc:         working with COVID-19 dataset
########################################################################

# import python modules that will be used in the code
import pandas as pd

# file location of the CSV file
file_location = "./data/heart_failure.csv"

# read the CSV into a pandas dataframe object
df = pd.read_csv(file_location)

# print shape of dataframe
num_rows, num_cols = df.shape
print("Successfully imported ", num_rows, " rows and ",
      num_cols, " columns and data.\n")

# print out all possible column headers
for col in df.columns:
    # print(col)
    pass

# get the number of deaths
num_deaths = sum(df["DEATH_EVENT"])

# print the number of positive/negative scenarios for heart failure
print("Dataset contains ", num_deaths, " events with heart failures and ",
      int(num_rows - num_deaths), " events without heart failure.\n")

# Use Bayes' theorem to calculate probability of heart failure given
# that the patient has diabetes in the dataset
# see https://en.wikipedia.org/wiki/Bayes%27_theorem
# P(A) = probability of heart failure
# P(B) = probability of diabetes

prob_heart_failure = num_deaths / num_rows
prob_diabetes = sum(df["diabetes"]) / num_rows

# filter DataFrame to only include rows with both death and diabetes
filtered_df = df[(df["DEATH_EVENT"] == 1) & (df["diabetes"] == 1)]

# probability of diabetes given heart failure
prob_B_given_A = len(filtered_df) / num_deaths

prob_death_given_diabetes = prob_B_given_A * prob_heart_failure \
                          / prob_diabetes

# print out the probability
print("There is a ", round(prob_death_given_diabetes*100,2),
      "% probability that a patient will experience heart failure ",
      "provided they have diabetes.\n")
