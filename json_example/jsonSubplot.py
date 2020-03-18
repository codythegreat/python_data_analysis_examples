# jsonTest.py - pulls data from a json file and plots
#               male and female acocunt balances using
#               plotly subplots. 
#               Uses MOCK_DATA.json

import json
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# data will hold our json data
data = json.load(open('MOCK_DATA.json'))

# assign money values to list as float data type
maleBalances = []
femaleBalances = []
for person in data:
    for key, value in person.items():
        if key == "gender" and value == "F":
            # convert to float (excluding dollar sign)
            femaleBalances.append(float(person.get("balance")[1:]))
        elif key == "gender" and value == "M":
            # convert to float (excluding dollar sign)
            # I added 10K to each amount to showcase how real data can show biases
            maleBalances.append(float(person.get("balance")[1:])+10000)

# Create a figure with two subplots
fig = make_subplots(rows=1, cols=2)

# add female balance data to our left subplot
fig.add_trace(
    go.Scatter(
        x=np.arange(1, len(femaleBalances)+1),
        y=femaleBalances,
        mode="markers",
        name="Female (avg = $%s)" % "{:.2f}".format(np.mean(femaleBalances))
    ),
    row=1, col=1
)

# add male balance data to our left subplot
fig.add_trace(
    go.Scatter(
        x=np.arange(1, len(maleBalances)+1),
        y=maleBalances,
        mode="markers",
        name="Male (avg = $%s)" % "{:.2f}".format(np.mean(maleBalances))
    ),
    row=1, col=2
)

fig.show()