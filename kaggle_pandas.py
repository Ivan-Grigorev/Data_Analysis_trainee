import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime
from kaggle_pd_plt import *

pd.set_option('display.max_columns', 30)
pd.set_option('display.width', 1000)

data_rent = pd.read_csv('house_rent_dataset.csv')
data_airbnb = pd.read_csv('Airbnb_Open_Data.csv', low_memory=False)

"""
print(data_rent.loc[0:5, :'Rent'])
print(data_rent[(data_rent['Posted On'] > str(datetime(year=2022, month=5, day=1))) &
                (data_rent['Posted On'] < str(datetime(year=2022, month=5, day=3)))]
      [:10])

print(data_rent.loc[data_rent['Rent'] > 10000][:10].sort_values('Rent', ascending=True))
print(data_rent.loc[data_rent['Point of Contact'] != 'Contact Owner'][:10])
print(data_rent.size)
data_rent.at[2345, 'Rent'] = 11200
print(data_rent.at[2345, 'Rent'])
print(data_rent.loc[1])
data_rent['Rent'][data_rent.loc[data_rent['Rent'] > 20000].index] = 'Expensive'
a = data_rent.loc[:, :'Rent'].tail()
a['Rent'][a.loc[a['Rent'] > 30000].index] = 'Expensive'
print(data_rent['Rent'].idxmax())
print(data_rent.loc[data_rent['rEnt'.capitalize()].idxmin()],
      data_rent.loc[data_rent['Rent'].idxmax()],
      data_rent['Rent'].median(), sep='\n')
print(data_rent['Point of Contact'].value_counts())
print(data_rent.head().add_prefix('<<-').add_suffix('->>'))
print(data_rent.drop(
    [i for i in data_rent[data_rent['Rent'] < 10000].index.__dict__['_data']],
    axis=0)
)
print(data_rent.nlargest(5, 'Rent'))
print(data_rent.nsmallest(5, 'Rent'))
print(data_rent.to_xarray())  # pipenv install xarray
print(data_rent.T)
print(data_rent.shift(periods=3).head())
print(data_rent.sort_values('Rent', ascending=False).head(10))
data_for_line = data_rent[(data_rent['Posted On'] > str(datetime(year=2022, month=6, day=1))) &
                          (data_rent['Posted On'] < str(datetime(year=2022, month=6, day=30)))] \
    .drop_duplicates('Posted On') \
    .sort_values('Posted On') \
    .set_index(i for i in range(1, 30))
data_view = pd.DataFrame({
    'Rent': [y for y in data_for_line['Rent']]
}, index=[x for x in data_for_line['Posted On']])
print(data_view.plot.line())
plt.plot(
      [x for x in data_for_line['Posted On']],
      [y for y in data_for_line['Rent']],
)
plt.show()

print(data_airbnb['neighbourhood group'].astype(str).str.capitalize().drop_duplicates())
"""

manhattan_data = data_airbnb[data_airbnb['neighbourhood group'] == 'Manhattan'].head(5)
# print(manhattan_data['number of reviews'].sum() / len(manhattan_data))
# print([i.split('/') for i in manhattan_data['last review'] if type(i) == str])
# print(result_manhattan['number of reviews'][result_manhattan.index[0]])
# print(data_airbnb[(data_airbnb['lat'] == 40.7256) &
#                   (data_airbnb['long'] == -73.99445)], '\n')
# print(data_airbnb[(data_airbnb['lat'] == 40.74771) &
#                   (data_airbnb['long'] == -73.94740)], '\n')

