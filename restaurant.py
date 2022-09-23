#The purpose of this analysis with python is to determine from an available dataset of 20 restaurant, what cuisine and category/package was bought more by customers

import numpy as np

import pandas as pd

#import the dataset
df = pd.read_excel(r'/Users/great ness/Desktop/Restraurant/Restaurants.xlsx')

#this prints the first 5 rows in the dataset
print(df.head())

#this gets the total values of data in the category and cuisine column
e = df['Category'].value_counts()
print(e)


f= df['Cuisine'].value_counts()
print(f)

#begin to set the parameters for the data visualiztion
import matplotlib.pyplot as plt
plt_1 = plt.figure(figsize=(16, 9))
plt.style.use('fivethirtyeight')


#this plots a horizontal bar chart based on data gotten from the cuisine column
f.plot(kind= 'barh', x = 'Pro', y='Ordinary', alpha=0.6)

#plt.pie(list,explode = [0,0.1],autopct='%.2f%%', colors= colors,shadow = True)
plt.title('Restaurants order',fontsize=14)
plt.ylabel('')
plt.xticks(rotation=90)

plt.xlabel('')

#plt.legend(labels1, loc='upper left')
labels = ['Cuisine']
plt.legend(labels, loc = 'upper right')
plt.savefig('restr.png')
plt.show()


#now create a pie chat that gives a visual representation of what category customers ordered

a = df['Category'].value_counts()

import matplotlib.pyplot as plt

plt_1 = plt.figure(figsize=(16, 9))
plt.style.use('ggplot')
list = a
labels1 = ['Percentage of those that ate Ordinary cuisine category', 'Percentage of those that ate Pro cuisine category']

colors = ['#7590a3','lightblue']

plt.pie(list,explode = [0,0.1],autopct='%.2f%%', colors= colors,shadow = True)

plt.title('Restaurants Analysis',fontsize=15)
plt.ylabel('')
plt.xticks(rotation=90)

plt.xlabel('')

plt.legend(labels1, loc='lower left')


plt.savefig('restpie.png')
plt.show()
