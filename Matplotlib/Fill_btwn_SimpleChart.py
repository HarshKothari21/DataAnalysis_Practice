import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data1.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

# overall_median = 57287
#fill_between fills the color if where not specified it fills color all the way down.
plt.fill_between(ages, py_salaries, dev_salaries, label='Above Avg',
	where=(py_salaries > dev_salaries), interpolate=True, alpha=0.25)

plt.fill_between(ages, py_salaries, dev_salaries, label='Below Avg',
	where=(py_salaries <= dev_salaries), interpolate=True, alpha=0.25)

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()