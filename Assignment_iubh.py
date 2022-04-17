import sqlite3
from matplotlib import pyplot as plt
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Float, Integer, Table, select, MetaData
from sqlalchemy.orm import sessionmaker
import csv
import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt
import numpy as np
from sklearn.linear_model import LinearRegression
import pandas_bokeh
from bokeh.plotting import figure, output_file, show



engine = create_engine('sqlite:///assignment.sqlite1', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()

Ideal = declarative_base()
class Listing(Ideal):
    __tablename__ = 'idealfun'
    id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)
    y5 = Column(Float)
    y6 = Column(Float)
    y7 = Column(Float)
    y8 = Column(Float)
    y9 = Column(Float)
    y10 = Column(Float)
    y11 = Column(Float)
    y12 = Column(Float)
    y13 = Column(Float)
    y14 = Column(Float)
    y15 = Column(Float)
    y16 = Column(Float)
    y17 = Column(Float)
    y18 = Column(Float)
    y19 = Column(Float)
    y20 = Column(Float)
    y21 = Column(Float)
    y22 = Column(Float)
    y23 = Column(Float)
    y24 = Column(Float)
    y25 = Column(Float)
    y26 = Column(Float)
    y27 = Column(Float)
    y28 = Column(Float)
    y29 = Column(Float)
    y30 = Column(Float)
    y31 = Column(Float)
    y32 = Column(Float)
    y33 = Column(Float)
    y34 = Column(Float)
    y35 = Column(Float)
    y36 = Column(Float)
    y37 = Column(Float)
    y38 = Column(Float)
    y39 = Column(Float)
    y40 = Column(Float)
    y41 = Column(Float)
    y42 = Column(Float)
    y43 = Column(Float)
    y44 = Column(Float)
    y45 = Column(Float)
    y46 = Column(Float)
    y47 = Column(Float)
    y48 = Column(Float)
    y49 = Column(Float)
    y50 = Column(Float)

Ideal.metadata.drop_all(bind=engine)
Ideal.metadata.create_all(engine)

try:
    with open('ideal_fun.csv', encoding='utf-8', newline='') as csv_file:
        csvreader = csv.DictReader(csv_file, quotechar='"',)
        listings = [Listing(**row) for row in csvreader]
        session.add_all(listings)
except FileNotFoundError:
    print('File not found!!', 'ideal_fun.csv')



Trng = declarative_base()
class Training(Trng):
    __tablename__ = 'trngfun'
    id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)

Trng.metadata.drop_all(bind=engine)
Trng.metadata.create_all(engine)

try:
    with open('trainingdata.csv', encoding='utf-8', newline='') as csv_file:
        csvreader = csv.DictReader(csv_file, quotechar='"',)
        listings = [Training(**row) for row in csvreader]
        session.add_all(listings)
except FileNotFoundError:
    print('File not found!!', 'trainingdata.csv')



Tst = declarative_base() 
class Test(Tst):
    __tablename__ = 'testfun'
    id = Column(Integer, primary_key=True)
    x = Column(Integer)
    y1 = Column(Float)

Tst.metadata.drop_all(bind=engine)
Tst.metadata.create_all(engine)

try:
    with open('testdata.csv', encoding='utf-8', newline='') as csv_file:
        csvreader = csv.DictReader(csv_file, quotechar='"',)
        listings = [Test(**row) for row in csvreader]
        session.add_all(listings)
except FileNotFoundError:
    print('File not found!!', 'testdata.csv')


        
session.commit()
session.close()

df = round(pd.read_sql_table('idealfun', con=engine), 2)
df1 = round(pd.read_sql_table('trngfun', con=engine), 2)
df2 = round(pd.read_sql_table('testfun', con=engine), 2)

print("\nIdeal function s data: df(50 colx100rowa\n")
print(df)
print("\nTainnng function s data: df1(4 colx100rowa\n")
print(df1)
print("\nTest function s data: df2(01 colx100rowa\n")
print(df2)

n = 2
while n < 6:
    df1.rename(columns={df.columns[n]: 'ya{}'.format(n-1)}, inplace=True)
    n=n+1
print("\n Training function after columns renamning: df1\n")
print(df1)

print("\nafter joining two data frames in panda:df3 = df+df1\n")

cols = ['y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8','y9','y10',
    'y11', 'y12', 'y13', 'y14','y15','y16', 'y17', 'y18', 'y19', 'y20',
    'y21', 'y22', 'y23', 'y24', 'y25', 'y26', 'y27', 'y28', 'y29', 'y30',
    'y31', 'y32', 'y33', 'y34', 'y35', 'y36', 'y37', 'y38', 'y39', 'y40',
    'y41', 'y42', 'y43', 'y44', 'y45', 'y46', 'y47', 'y48', 'y49', 'y50']

class MathO():
    def __init__(self, df_1, df_2):
        self.df1 = df_1
        self.df2 = df_2

    def join_func(self):
        frames = [self.df1, self.df2]
        z=pd.concat(frames, axis=1, join='inner')
        return z

    def sqr_dev(self,p):
        x = MathO(df,df1)
        z = x.join_func()
        for c in cols:
            z[c]= round(((z[p]-z[c])**2), 2)
        z = z.iloc[:, :-6]
        return z
   
x = MathO(df,df1)
df3 = x.join_func()
print(df3)

def sum_columns(p):
    y=p.copy(deep=True)
    for c in cols:
        y[c] = y[c].sum()
    y=y.drop(y.index[1:100], axis=0)
    y=y.iloc[:, 2:]
    return y

print("\n1. deviations squred between ideal(50) func and ya1:df4\n")
df4 = x.sqr_dev('ya1')
print(df4)
print("\nY 2. deviations squred between ideal(50) func and ya2:df5\n")
df5 = x.sqr_dev('ya2')
print(df5)
print("\nY 3. deviations squred between ideal(50) func and ya3:df6\n")
df6 = x.sqr_dev('ya3')
print(df6)
print("\nY 4. deviations squred between ideal(50) func and ya4:df7\n")
df7 = x.sqr_dev('ya4')
print(df7)

df8 = sum_columns(df4)
df9 = sum_columns(df5)
df10 = sum_columns(df6)
df11 = sum_columns(df7)

print("\n Afeter joining four rows of deviation sums:df12\n ")
frames = [df8, df9, df10, df11]
df12 = pd.concat(frames, axis=0)
print(df12)


print("\n column values corresponding to min values in row:df15\n")
cols = [df12.idxmin(axis=1)]
for c in cols:
    df15 = (df[c])

print(df15)

print("\n Selected functions with x column added::df16\n")

df16 = df15.copy(deep=True)
data = list(range(1, 101, 1))
df16.insert(0, 'x', data)
print(df16)

print("\nSquare of y deviations correspondind to Ideal functions that minimizes the y deviations for four trg func:df22")
df18 = df4[df15.columns[0]]
df19 = df5[df15.columns[1]]
df20 = df6[df15.columns[2]]
df21 = df7[df15.columns[3]]

frames = [df18, df19, df20, df21]
df22 = pd.concat(frames, axis=1)

print(df22)

print("\n Max deviation in each column selected for four trg fumc:df23\n")

df23 = df22.max()
print(df23)

print("\n Predicted values: df24\n")

def lin_reg(p):
    X = np.array([df16.iloc[:,0]]).reshape((-1, 1)) 
    y = np.array(df16.iloc[:,p]) 
    model = LinearRegression() 
    model.fit(X,y)
    y_pred = model.predict(X)
    return y_pred

def convert_arr(x,y):
    z = lin_reg(x)
    z = pd.DataFrame(z,columns = [y])
    return z

df24 = convert_arr(1,df22.columns[0])
df25 = convert_arr(2,df22.columns[1])
df26 = convert_arr(3,df22.columns[2])
df27 = convert_arr(4,df22.columns[3])

frames = [df24, df25, df26, df27]
df28 = pd.concat(frames, axis=1)


df29 = df2.copy(deep = True)
df29.rename(columns={df.columns[2]: 'y_test'},inplace=True)
df30 = df29.drop(columns=["x","id"])
frames = [df28, df30]
df31 = round((pd.concat(frames, axis=1,join = 'inner')),2)
print("\n Final table with predicted values of corresponding selected functions:df31\n")
print(df31)

df32 = df31.copy(deep = True)

print("\n deviations from actual and predicted values:df32\n")
n=0
while n < 4:
    df32.iloc[:,n]= abs(df32.iloc[:,4]-df32.iloc[:,n])
    n = n+1
print(df32)

print("\n maximum deviations between actual and predicted values and corresponding functions:df34\n")
df33 = df32.copy(deep=True)
df34 = df33.max()
print(df34)

print("\n")
n = 0
while n<4:
    if df34[n] <= df23[n]*sqrt(2):
        print(df34.index[n], ":is a suitable function:\n")
    else:
        print(df34.index[n], ":is not a suitable function:\n")
    n = n+1

print ("\n Plt show : df35\n")
df35 = df31.copy(deep=True)
data = list(range(1, 101, 1))
df35.insert(0, 'x', data)
df35.columns = ['x', '1st Func', '2nd_Func', '3rd_Func', '4th_Func', 'Test Func']
print(df35)  

def plot(p, q):
    output_file("gfg{}.html".format(p))
    graph = figure(title = "Bokeh Multi Line Graph")
    xs = [df35.iloc[:, 0], df35.iloc[:, 0]]
    ys = [df35.iloc[:, p], df35.iloc[:, 5]]
    graph.xaxis.axis_label = "x-axis"
    graph.yaxis.axis_label = "Test Data & {} Predicted Data".format(q)
    line_color = 'red', 'blue'
    graph.multi_line(xs, ys, line_color=line_color)
    return graph
    
show(plot(1, "1st"))
show(plot(2, "2nd"))
show(plot(3, "3rd"))
show(plot(4, "4th"))
