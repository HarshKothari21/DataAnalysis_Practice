from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]     #comes 0.1 part out of the chart
#colors = ['blue', 'red', 'yellow', 'green']

plt.pie(slices, labels=labels, explode=explode, shadow=True, startangle=90,
 	autopct='%1.1f%%', wedgeprops={'edgecolor' : 'black'})
#shadow gives 3d view of chart which is optional; startangle rotate chart starting from 90degree straight line.
#autoperct. gives percantage to the pie chart; wedgeprops gives some thin edge of black color

plt.title('My Pie Chart')
plt.tight_layout()
plt.show()