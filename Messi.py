Messi = list()
print(Messi)
while True:
    messi_goals = input('Give us the messi goals in a season:')
    print('messi goals in season 1 is:', messi_goals)
    if messi_goals == 'Done!':
        break
    goals = float(messi_goals)
    Messi.append(goals)
Average = sum(Messi)/len(Messi)
print('The Average goals scored by messi in a season is:', Average)
