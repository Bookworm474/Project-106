import pandas as pd
import numpy as np
import plotly.express as px
import csv

df = pd.read_csv("data3.csv")
fig = px.scatter(
    df,
    x="Marks In Percentage",
    y="Days Present"
)
fig.show()

with open("data3.csv", newline="") as f:
    reader = csv.reader(f)
    filedata = list(reader)
filedata.pop(0)
marks = []
days = []
for data in filedata:
    marks.append(float(data[1]))
    days.append(float(data[2]))
correlation = np.corrcoef(marks,days)
print(correlation[0,1])
#The data is directly correlated