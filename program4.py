import pandas as pd
import numpy as np
import plotly.express as px
import csv

df = pd.read_csv("data4.csv")
fig = px.scatter(
    df,
    x="Coffee in ml",
    y="sleep in hours"
)
fig.show()

with open("data4.csv", newline="") as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
coffee = []
sleep = []
for data in filedata:
    coffee.append(float(data[1]))
    sleep.append(float(data[2]))
correlation = np.corrcoef(coffee,sleep)
print(correlation[0,1])
#The data is inversely correlated