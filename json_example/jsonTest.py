import json
import numpy as np
import plotly.graph_objects as go

data = json.load(open('MOCK_DATA.json'))

# assign money values to list as float data type
numberData = []
for person in data:
    for key, value in person.items():
        if key == "balance":
            # convert to float (excluding dollar sign)
            numberData.append(float(value[1:]))

x = np.arange(1, 101)
print(x[1])

fig = go.Figure(go.Scatter(
    x = x,
    y = numberData
))

fig.update_layout(
    title = 'Random number data plotted to a scatter line'
)
fig.show()