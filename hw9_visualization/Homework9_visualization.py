## Homework 9: 

## Import
from array import array
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


## Ene graphic-iig harah
var = pd.read_excel(r'C:\Users\beegi\OneDrive\Python\Homework_fall\hw9_visualization\wdi.xlsx', sheet_name='gdp')
x   = list(var['year'])
y   = list(var['USA'])
#plt.ylim([0,5])
plt.plot(x,y)
plt.show()

## DON'T MIND
df = pd.read_excel(r'C:\Users\beegi\OneDrive\Python\Homework_fall\hw9_visualization\wdi.xlsx')
df[['year', 'USA']].plot.bar
plt.show()

var = pd.read_excel(r'C:\Users\beegi\OneDrive\Python\Homework_fall\hw9_visualization\wdi.xlsx', sheetname='debt')
x   = list(var['year'])
y   = list(var['USA'])
plt.plot(x,y)
plt.show()


var = pd.read_excel(r'C:\Users\beegi\OneDrive\Python\Homework_fall\hw9_visualization\wdi.xlsx', sheetname='reserve')
x   = list(var['year'])
y   = list(var['USA'])
plt.plot(x,y)
plt.show()


plt.title('yu ch yahve')
plt.xlabel()