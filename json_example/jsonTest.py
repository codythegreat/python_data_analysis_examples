import json
import numpy as np
import plotly.graph_objects as go

data = json.load(open('MOCK_DATA.json'))

# assign money values to list as float data type
maleBalances = []
femaleBalances = []
for person in data:
    print(person.items())
    for key, value in person.items():
        if key == "gender" and value == "F":
            # convert to float (excluding dollar sign)
            femaleBalances.append(float(person.get("balance")[1:]))
        elif key == "gender" and value == "M":
            # convert to float (excluding dollar sign)
            maleBalances.append(float(person.get("balance")[1:]))

x = np.arange(1, len(femaleBalances))
print(x[1])

fig = go.Figure(go.Scatter(
    x = x,
    y = femaleBalances
))

fig.update_layout(
    title = 'Female Balances'
)
fig.show()
