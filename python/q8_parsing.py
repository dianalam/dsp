# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

# The below skeleton is optional.  You can use it or you can write the script with an approach of your choice.

# solution with pandas
import pandas as pd
fball = pd.read_csv('football.csv') 

fball['GoalsDif'] = abs(fball['Goals'] - fball['Goals Allowed'])
minteam = fball.loc[fball['GoalsDif'].idxmin()]
print minteam.Team + ' had the smallest difference in for and against goals.'

# solution without pandas
import csv

with open ('football.csv') as fball:
    difdict = {}
    datadict = csv.DictReader(fball)
    for row in datadict:
        difdict[row['Team']] = abs(int(row['Goals']) - int(row['Goals Allowed']))

minteam = min(difdict.items(), key=lambda x:x[1])

print minteam[0] + ' had the smallest difference in for and against goals.'
