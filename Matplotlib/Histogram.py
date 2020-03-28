#hiatogram basically counts the number of data in given ranges
#in current data set i have ages ranging from 10 to 100. It automatically counts ages and show in graph format.

import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
data = pd.read_csv('data3.csv')
ids = data['Responder_id']
ages = data['Age']

#the argument log, gives the count in log form
plt.hist(ages, edgecolor='black', bins=bins, log=True)   #if you dont specify bins it will set it automatically 


median_age = 29
color = '#fc4f30'

plt.axvline(median_age, label='H-Meian', color=color, linewidth=2) #line width is optional, it just defines the line thickness

plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()