########################################################################
# Author(s):    D. Knowles
# Date:         26 Jul 2021
# Desc:         working with COVID-19 dataset
########################################################################

# import python modules that will be used in the code
import pandas as pd
import matplotlib.pyplot as plt


# file location of the CSV file
file_location = "./data/covid19.csv"

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

# get single column (series) of data from the dataframe
deaths = df["deaths_covid"]

# display number of deaths greater than 1000
num_large_deaths = sum(deaths > 1000)

# print the number of large deaths and largest death count
print("There were ", num_large_deaths, " reports of deaths >1000, "
      "the largest of which was ", int(deaths.max()), ".")

# for plotting we will remove the outliers
df = df[df["deaths_covid"] < 1000]

# calculate the percentage of hospitals understaffed and
# add new column to dataframe
df["percent_understaffed"] = df["critical_staffing_shortage_today_yes"]\
                           /(df["critical_staffing_shortage_today_no"] \
                           + df["critical_staffing_shortage_today_yes"])

# create histogram of the newly created dataframe column
df.hist(column="percent_understaffed", bins = 50)

# create new dataframes based on the percent of reporting hospitals
# that are understaffed
poorly_staffed = df[df["percent_understaffed"] >= 0.2]
well_staffed = df[df["percent_understaffed"] < 0.2]

# create a new figure that contains 1 row and 2 columns of subplots
fig, axes = plt.subplots(1,2)

# for the subplot at index 0, set the title
axes[0].title.set_text("well staffed")

# graph deaths vs. bed utilization for a well staffed hospital
well_staffed.plot.scatter(x = "inpatient_beds_utilization",
               y = "deaths_covid",
               c = "blue",
               ax=axes[0])

# for the subplot at index 1, set the title
axes[1].title.set_text("poorly staffed")

# graph deaths vs. bed utilization for a poorly staffed hospital
poorly_staffed.plot.scatter(x = "inpatient_beds_utilization",
               y = "deaths_covid",
               c = "red",
               ax=axes[1])

# have to include this line to show the plots and pause to view
plt.show()
