import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('datas.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0])
        y.append(row[1])

plt.plot(x,y,color="red")
plt.show()