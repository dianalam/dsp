###Part I - Regular Expressions  


####Q1. Find how many different degrees there are, and their frequencies: Ex:  PhD, ScD, MD, MPH, BSEd, MS, JD, etc.

import csv
import re
with open ('faculty.csv') as faculty:
    degrees = [] # create empty list to store degrees from file
    facDict = csv.DictReader(faculty)
    for row in facDict:
        degrees.append(row[' degree'])

# parsing...
degrees = [s.replace('.', '').strip() for s in degrees] # remove periods and spaces 
degreesSplit = [word for line in degrees for word in line.split()] # convert single strings with multiple degrees into separate strings
degreesSplit = [s for s in degreesSplit if not re.search(r'\d',s)] # remove the pesky 0

# count degrees
counter = {}
for d in degreesSplit:
    if d not in counter:
        counter[d] = 1
    else:
        counter[d] += 1  

# print results
print 'There are %d types of degrees.' % len(counter)
print 'Degree frequencies:', counter

####Q2. Find how many different titles there are, and their frequencies:  Ex:  Assistant Professor, Professor

with open ('faculty.csv') as faculty:
    titles = []
    facDict = csv.DictReader(faculty)
    for row in facDict:
        titles.append(row[' title'])

tcounter = {}
for t in titles:
    if t not in tcounter:
        tcounter[t] = 1
    else:
        tcounter[t] += 1

# print results
print 'There are %d types of titles.' % len(tcounter)
print 'Title frequencies:', tcounter

####Q3. Search for email addresses and put them in a list.  Print the list of email addresses.

with open ('faculty.csv') as faculty:
    emails = []
    facDict = csv.DictReader(faculty)
    for row in facDict:
        emails.append(row[' email'])

print emails


####Q4. Find how many different email domains there are (Ex:  mail.med.upenn.edu, upenn.edu, email.chop.edu, etc.).  Print the list of unique email domains.

unique_emails = {e.split('@')[1] for e in emails}
print unique_emails