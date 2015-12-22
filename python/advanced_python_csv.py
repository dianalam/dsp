import csv

# open and parse list of emails
with open ('faculty.csv') as faculty:
    emails = []
    facDict = csv.DictReader(faculty)
    for row in facDict:
        emails.append(row[' email'])

# write emails to new csv 
with open ('emails.csv', 'w') as newcsv:
	mywriter = csv.writer(newcsv)
	for item in emails:
		mywriter.writerow([item])
	newcsv.close()