import math
import numpy as np
import pandas as pd
import csv
print("FUNCTION : START Creating a CSV file")
x = np.arange(1, 101, 1)
file = open('data.csv','w', newline = "")
csvwriter = csv.writer(file)
csvwriter.writerow(x)
csvwriter.writerow(x)
n = 1
c = 1
y1 = []
while (n<11 and c<11):
    y1 = c*np.sin(n*x)
    y1 = [round(i, 2) for i in y1]
    csvwriter.writerow(y1)
    n = n+1
    c = c+1
file.close()
file = open('data.csv','a', newline = "")
csvwriter = csv.writer(file)
n = 1
y2 = []
while (n<11):
    y2 = x**2/n
    y2 = [round(i, 2) for i in y2]
    csvwriter.writerow(y2)
    n= n+1
n = 1
c = 1
y3 = []
while (n<11 and c <22):
    y3 = x**2 + n*x +c
    y3 = [round(i, 2) for i in y3]
    csvwriter.writerow(y3)
    n= n+1
    c = c+2
n = 1
c = 1
y4 = []
while (n<11 and c<11):
    y4 = n*x + c
    y4 = [round(i, 2) for i in y4]
    csvwriter.writerow(y4)
    n = n+1
    c = c+1
n = 1
c = 1
y5 = []
while (n<11 and c<110):
    y5 = n*np.log10(x) + c
    y5 = [round(i, 2) for i in y5]
    csvwriter.writerow(y5)
    n = n+1
    c = c+10
file.close()
df = pd.read_csv('data.csv') 
df1 = df.T

df1.columns = ['x','y1', 'y2', 'y3','y4','y5','y6','y7', 'y8','y9','y10',
    'y11', 'y12', 'y13','y14','y15','y16', 'y17','y18','y19','y20',
    'y21', 'y22', 'y23','y24','y25','y26','y27','y28','y29','y30',
    'y31','y32','y33','y34','y35','y36','y37','y38','y39','y40',
    'y41','y42','y43','y44','y45','y46','y47','y48','y49','y50']

print(df1)

df1.to_csv('ideal_fun.csv', index = False)
print("--------END---------")