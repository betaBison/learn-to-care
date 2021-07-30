########################################################################
# Author(s):    D. Knowles
# Date:         26 Jul 2021
# Desc:         working with Ehlers Danlos dataset
########################################################################

# import python modules that will be used in the code
import pandas as pd
import matplotlib.pyplot as plt


# file location of the CSV file
file_location = "./data/pain.csv"

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

# only use completed surveys
df = df[df["Complete?"] == "Complete"]

# calculate number of answers to the survey
num_rows = df.shape[0]  # or len(df)

# create dictionary to store most common pain treatments
percent_use = {}

# calculate the percent of patients who used acetaminophen
percent_acetaminophen = sum(df["Have you ever used Acetaminophen " \
                      + "(brand name Tylenol) to treat your chronic " \
                      + "pain?"] == "Yes") / num_rows

# add to dictionary
percent_use["acetaminophen"] = percent_acetaminophen * 100

# repeat for other types of pain management (there's loads)
percent_NSAIDs = sum(df["Have you ever used NSAIDs to treat your " \
               + "chronic pain? (nonsteroidal anti-inflammatory drugs" \
               + " such as aspirin, ibuprofen, aleve, etc.)"] == "Yes")\
               / num_rows
percent_use["NSAIDs"] = percent_NSAIDs * 100

percent_physical = sum(df["Have you ever used Physical therapy or " \
                 + "physiotherapy to treat your chronic "
                 + "pain?"] == "Yes") / num_rows
percent_use["physical therapy"] = percent_physical * 100

percent_marijuana = sum(df["Have you ever used a form of Marijuana to "\
                  + "treat your chronic pain?"] == "Yes") / num_rows
percent_use["marijuana"] = percent_marijuana

percent_marijuana = sum(df["Have you ever used a form of Marijuana to "\
                  + "treat your chronic pain?"] == "Yes") / num_rows
percent_use["marijuana"] = percent_marijuana * 100

percent_tai_chi = sum(df["Have you ever used Tai Chi to treat your " \
                + "chronic pain? (series of movements performed in a "\
                + "slow, focused manner and accompanied by deep "\
                + "breathing)"] == "Yes") / num_rows
percent_use["Tai Chi"] = percent_tai_chi * 100

# extract keys and values from dictionary
keys = percent_use.keys()
values = percent_use.values()

# create a bar graph to illustrate results
plt.bar(keys,values)
plt.ylabel("Percent use by patients.")

# have to include this line to show the plots and pause to view
plt.show()
