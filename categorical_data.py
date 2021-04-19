import pandas as pd
import numpy as np

# presence data
stat = pd.read_csv("participation.csv")

# Frequency calculation
stat_freq = stat[stat["Attend"] == 1]["Name"].value_counts()
print("present Frequency calculation")
print(stat_freq.to_string())
print("\r\n")

# Relative Frequency calculation
stat_relfreq = stat[stat["Attend"] == 1]["Name"].value_counts(normalize=True)
print("Relative Frequency calculation")
print(stat_relfreq.to_string())
print("\r\n")

# Frequency Table that checks total attend count
stat_tab = pd.crosstab(index=stat["Attend"], columns="count")
print("Frequency Table that checks total attend count")
print(stat_tab)
print("\r\n")

# Frequency Table, how many people are attended?
stat_who = pd.crosstab(index=stat["Attend"], columns=stat["Name"])
print("Frequency Table, how many people are attended?")
print(stat_who)
print("\r\n")