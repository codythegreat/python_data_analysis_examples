import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from random import randrange

def convertCaloriesToWeight(calories):
    return (calories-2000)/3000

calorieIntake = []

for i in range(90):
    calorieIntake.append(2000 + (3*randrange(100) - 2*randrange(100)))

weightOverTime = [float(160)]

for i in range(89):
    weightOverTime.append(weightOverTime[i] + convertCaloriesToWeight(calorieIntake[i]))

x = np.arange(1, 91)

fig = make_subplots(rows=1, cols=2)

fig.add_trace(go.Scatter(x=x, y=calorieIntake,
                    mode="lines+markers",
                    name="Daily Calorie Intake"),
                    row=1, col=1
)

fig.add_trace(go.Scatter(x=x, y=weightOverTime,
                    mode="lines+markers",
                    name="Weight Over Time"),
                    row=1, col=2
)

fig.show()