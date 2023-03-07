import pandas as pd
import numpy as np

import matplotlib.pyplot as plt


pd.set_option("display.max_columns", 30)
pd.set_option("display.width", 1000)

data_airbnb = pd.read_csv("../CSV/Airbnb_Open_Data.csv", low_memory=False)

sorted_data = data_airbnb[data_airbnb["price"] != "NaN"].drop_duplicates(subset="price")

sorted_manhattan = sorted_data[sorted_data["neighbourhood group"] == "Manhattan"]
result_manhattan = (
    sorted_manhattan[sorted_manhattan["Construction year"] >= 2020]
    .sort_values("price", ascending=False)
    .head(5)
)
print(result_manhattan, "\n")

sorted_queens = sorted_data[sorted_data["neighbourhood group"] == "Queens"]
result_queens = (
    sorted_queens[sorted_queens["Construction year"] >= 2020]
    .sort_values("price", ascending=False)
    .head(5)
)
print(result_queens, "\n")

sorted_st_island = sorted_data[sorted_data["neighbourhood group"] == "Staten Island"]
result_st_island = (
    sorted_st_island[sorted_st_island["Construction year"] >= 2020]
    .sort_values("price", ascending=False)
    .head(5)
)
print(result_st_island, "\n")

sorted_brooklyn = sorted_data[sorted_data["neighbourhood group"] == "Brooklyn"]
result_brooklyn = (
    sorted_brooklyn[sorted_brooklyn["Construction year"] >= 2020]
    .sort_values("price", ascending=False)
    .head(5)
)
print(result_brooklyn, "\n")

sorted_bronx = sorted_data[sorted_data["neighbourhood group"] == "Bronx"]
result_bronx = (
    sorted_bronx[sorted_bronx["Construction year"] >= 2020]
    .sort_values("price", ascending=False)
    .head(5)
)
print(result_bronx, "\n")

"""
    One column bar
    
x = ['Manhattan', 'Brooklyn', 'Staten Island', 'Queens', 'Bronx']
y = [int((result_manhattan['price'][result_manhattan.index[0]])
         .removeprefix('$')
         .replace(',', '')),
     int((result_brooklyn['price'][result_brooklyn.index[0]])
         .removeprefix('$')
         .replace(',', '')),
     int((result_st_island['price'][result_st_island.index[0]])
         .removeprefix('$')
         .replace(',', '')),
     int((result_queens['price'][result_queens.index[0]])
         .removeprefix('$')
         .replace(',', '')),
     int((result_bronx['price'][result_bronx.index[0]])
         .removeprefix('$')
         .replace(',', ''))]

plt.bar(x, y, color=['blue', 'red', 'orange', 'green', 'yellow'])

for ind, val in enumerate(y):
    plt.text(ind, val, '$' + str(val), horizontalalignment='center', fontdict={'size': 15})
"""

"""
    Multiply bar plots
"""

bar_width = 0.30
fig, ax = plt.subplots(figsize=(14, 8))

price = [
    int(
        (result_manhattan["price"][result_manhattan.index[0]])
        .removeprefix("$")
        .replace(",", "")
    ),
    int(
        (result_brooklyn["price"][result_brooklyn.index[0]])
        .removeprefix("$")
        .replace(",", "")
    ),
    int(
        (result_st_island["price"][result_st_island.index[0]])
        .removeprefix("$")
        .replace(",", "")
    ),
    int(
        (result_queens["price"][result_queens.index[0]])
        .removeprefix("$")
        .replace(",", "")
    ),
    int(
        (result_bronx["price"][result_bronx.index[0]])
        .removeprefix("$")
        .replace(",", "")
    ),
]
service_fee = [
    int(
        (result_manhattan["service fee"][result_manhattan.index[0]])
        .removeprefix("$")
        .replace(",", "")
    ),
    int(
        (result_brooklyn["service fee"][result_brooklyn.index[0]])
        .removeprefix("$")
        .replace(",", "")
    ),
    int(
        (result_st_island["service fee"][result_st_island.index[0]])
        .removeprefix("$")
        .replace(",", "")
    ),
    int(
        (result_queens["service fee"][result_queens.index[0]])
        .removeprefix("$")
        .replace(",", "")
    ),
    int(
        (result_bronx["service fee"][result_bronx.index[0]])
        .removeprefix("$")
        .replace(",", "")
    ),
]
number_of_reviews = [
    result_manhattan["number of reviews"][result_manhattan.index[0]].__round__(),
    result_brooklyn["number of reviews"][result_brooklyn.index[0]].__round__(),
    result_st_island["number of reviews"][result_st_island.index[0]].__round__(),
    result_queens["number of reviews"][result_queens.index[0]].__round__(),
    result_bronx["number of reviews"][result_bronx.index[0]].__round__(),
]

val_1 = np.arange(len(price))
val_2 = [x + bar_width for x in val_1]
val_3 = [x + bar_width for x in val_2]

column_1 = plt.bar(
    val_1,
    price,
    color="blue",
    width=bar_width,
    edgecolor="black",
    label="Price $ per sq/m",
)
column_2 = plt.bar(
    val_2,
    service_fee,
    color="red",
    width=bar_width,
    edgecolor="black",
    label="Service fee $",
)
column_3 = plt.bar(
    val_3,
    number_of_reviews,
    color="yellow",
    width=bar_width,
    edgecolor="black",
    label="Number of reviews",
)

plt.xlabel("Islands of City", fontdict={"size": 15})
plt.xticks(
    [r + bar_width for r in range(len(price))],
    ["Manhattan", "Brooklyn", "Staten Island", "Queens", "Bronx"],
)
plt.ylabel("Amount", fontdict={"size": 15})
plt.ylim(-5, 1200)
plt.title(
    "The overview of real estate prices in New York City",
    fontdict={"size": 20, "color": "blue"},
)

ax.yaxis.grid(True, color="#EEEEEE", linestyle="-", linewidth=0.5)
ax.set_axisbelow(True)

ax.bar_label(column_1, padding=2)
ax.bar_label(column_2, padding=2)
ax.bar_label(column_3, padding=2)

fig.tight_layout()
plt.legend()
plt.show()
