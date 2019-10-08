from openpyxl import load_workbook
from openpyxl.styles import PatternFill
import pprint
import re

wb = load_workbook(filename = 'Football-2019.xlsx') # todo : add in worksheet names
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
winsByWeekByPlayer = dict() 
for ws in workSheets:
    colCounter = 2
    # create a new key to week with an empty string value
    winsByWeekByPlayer[ws] = []
    for player in players:
            # new list to hold each pick score
        scoreByGame = []
        for row in range(2, 19):
            # since some weeks are shorter, break when reach score
            if re.search(r"^\s*\d+-\d+\s*$", wb[ws].cell(row=row, column=colCounter).value):
                break
            # determine win by fill color
            if wb[ws].cell(row=row, column=colCounter).fill.fill_type == 'solid':
                scoreByGame.append(1)
            elif wb[ws].cell(row=row, column=colCounter).fill.fill_type == None:
                scoreByGame.append(0)
        colCounter = colCounter + 1
        winsByWeekByPlayer[ws].append({player[:3].upper(): scoreByGame})

pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(winsByWeekByPlayer[1])
print(winsByWeekByPlayer['Week 4'][-1])