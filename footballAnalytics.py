from openpyxl import load_workbook
from openpyxl.styles import PatternFill

wb = load_workbook(filename = 'book1.xlsx') # todo : add in worksheet names
workSheets = []
teams = []
# fill teams list with lists of [team1, team2, winner]
for ws in workSheets:
    for row in range(2, 16):
        gameData = []
        gameData.append(wb.ws['A'+str(row)].value.split(' at '))
        gameData.append(wb.ws['M'+str(row)].value)
        teams.append(gameData)

players = []
# fill players list from spreadsheet
for col in range(2, 12):
    players.append(wb.active['A'+str(col)].value)
# create a new dictionary holding each players game scores by week
winsByWeekByPlayer = dict() 
for ws in workSheets:
    colCounter = 2
    for week in range(1, 8):
        # create a new key to week with an empty string value
        winsByWeekByPlayer[week] = []
        for player in players:
            # new list to hold each pick score
            scoreByGame = []
            for row in range(2, 16):
                scoreByGame.append(wb.ws.cell(row=row, column=colCounter).value)
                # test to see if this works: determine win by fill color
                # if it doesn't try start_color
                if wb.ws.cell(row=row, column=colCounter).fill.fill_type == none:
                    scoreByGame.append(0)
                else:
                    scoreByGame.append(1)
            colCounter = colCounter + 1
            winsByWeekByPlayer[week].append({player: scoreByGame})
