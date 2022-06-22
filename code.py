import numpy as np
import csv
import plotly.express as px
import pandas as pd

df = pd.read_csv("data.csv")
x = df["Marks In Percentage"].tolist()
y = df["Days Present"].tolist()
fig = px.scatter(df, x = x, y = y)
fig.show()
# very less relationship is present between the data