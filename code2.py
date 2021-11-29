import pandas as pd
import csv
import plotly.express as go

data = pd.read_csv("data.csv")
data1 = data.groupby(["student_id","level"],as_index = False)["attempt"].mean()

print(data1)

fig = go.scatter(data1, x = "student_id", y = "level", size ='attempt',color = 'attempt')
fig.show()