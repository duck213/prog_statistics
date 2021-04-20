import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from matplotlib.colors import Normalize

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

# extracting non-duplicated name list
name_list = stat.iloc[:,[1]].drop_duplicates().Name.to_list()

# percentage
freq_percent = [int(round(i, 2)*100) for i in stat_relfreq]
fig = plt.figure()
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)

ax1.pie(freq_percent, labels=name_list)
ax1.axis('equal')

my_cmap = cm.get_cmap('jet')
my_norm = Normalize(vmin=0, vmax=60)
ax2.bar(name_list, freq_percent, color=my_cmap(my_norm(freq_percent)))
plt.show()

