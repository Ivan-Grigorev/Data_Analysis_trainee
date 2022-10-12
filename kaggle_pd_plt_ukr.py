import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime


pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 2000)
pd.set_option('display.max_columns', 30)

data = pd.concat([pd.read_csv('UKR_refugee_by_countries.csv'),
                  pd.read_csv('UKR_refugee_by_countries(1).csv'),
                  pd.read_csv('UKR_refugee_by_countries(2).csv')])

start_date = str(datetime(year=2022, month=2, day=24))
end_date = str(datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day))

source_unhcr = data[data['source'].values == 'UNHCR, Government']
source_other = data[data['source'].values == '0'].replace('0', 'Other')
country = 'Republic of Moldova'

sorted_by_date_unhcr = source_unhcr[(source_unhcr['date'] > start_date) &
                                    (source_unhcr['date'] < end_date)]
sorted_by_date_other = source_other[(source_other['date'] > start_date) &
                                    (source_other['date'] < end_date)]

sorted_by_source = pd.concat([sorted_by_date_other, sorted_by_date_unhcr])
sorted_by_country = sorted_by_source[sorted_by_source['country'] == country].drop_duplicates(subset=['date'])
# print(data.info())
print(sorted_by_country.sort_values('date', ascending=True))
