import matplotlib.pyplot as plt
from openpyxl import load_workbook
from openpyxl.styles import PatternFill
import pprint
import re
import numpy as np

wb = load_workbook(filename = 'Football-2019.xlsx')
workSheets = wb.sheetnames[:5]
teams = []
# fill teams list with lists of [team1, team2, winner]
for ws in workSheets:
    for row in range(2, 16):
        gameData = wb[ws]['A'+str(row)].value.split(' at ')
        gameData.append(wb[ws]['M'+str(row)].value)
        teams.append(gameData)

players = []
# fill players list from spreadsheet
for col in range(2, 13):
    players.append(wb.active.cell(column=col, row=1).value)
# create a new dictionary holding each players game scores by week
winsByWeekByPlayer = []
# add 5 empty lists to hold each weeks game data 
for week in range(0, 5):
    winsByWeekByPlayer.append([])
for ws in workSheets:
    colCounter = 2
    for player in players:
        # new list to hold each pick score
        scoreByGame = []
        for row in range(2, 19):
            # since some weeks are shorter, break when reach score
            if re.search(r"^\s*\d+-\d+\s*$", wb[ws].cell(row=row, column=colCounter).value):
                break
            # determine win by fill color
            if wb[ws].cell(row=row, column=colCounter).fill.fill_type == 'solid':
                scoreByGame.append(0)
            elif wb[ws].cell(row=row, column=colCounter).fill.fill_type == None:
                scoreByGame.append(1)
        colCounter = colCounter + 1
        winsByWeekByPlayer[workSheets.index(ws)].append(scoreByGame)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(winsByWeekByPlayer)
for p in range(0, 11):
    playerValues = []
    score = 0
    for week in winsByWeekByPlayer[1:]:
        for data in week[p]:
            score += data
        playerValues.append(score)
        score = 0
    print(playerValues)
    label = "player " + str(p)
    plt.plot([1,2,3,4], playerValues, label=label)
plt.legend()
plt.show()