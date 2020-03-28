from matplotlib import pyplot as plt

#print(plt.style.availabel) #prints differnet style availabel in matplotlib
#plt.style.use('fivethirtyeight')
plt.xkcd()      #gives comic style to graph

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]

#For plotting you can use labels to latel the line, color to give color to line, linestyle to give it doted or dashed
#Use matplotlib documentation to acknowledge yourself with different types of linewidth and color and marker 
#plot given in order will plot the line one after the other 
plt.plot(ages_x, py_dev_y, 'b', linewidth=3, label='Python')   

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583]

plt.plot(ages_x, js_dev_y, color='#adad3b', linewidth=3, label='Java')


dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]

plt.plot(ages_x, dev_y, color='#444444', linestyle='--', label='All Devs')

plt.title('Median Salary by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary')
plt.legend()   #necessary to give labels to the line/ You can also pass label as argument inside legend

plt.tight_layout()    #Used when ghraph is not fit in screen
#plt.grid(True)    #if you are not using styles then this will get a grid line in graph

plt.show()
#plt.savefig('plot.png')   #saves graph in current directory