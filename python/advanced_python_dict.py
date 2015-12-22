import csv

faculty_dict = {} 
professor_dict = {}

with open ('faculty.csv') as faculty:
    csvdict = csv.DictReader(faculty)
    for row in csvdict:

    	# faculty_dict work
        surname = row['name'].split()[-1] # create var for last name
        if surname in faculty_dict:
            faculty_dict[surname].append([row[' degree'], row[' title'], row[' email']])
        else:
            faculty_dict[surname] = [row[' degree'], row[' title'], row[' email']]
        
        # professor_dict work
        firstname = row['name'].split()[0]
        if (firstname, surname) in professor_dict:
            professor_dict[(firstname, surname)].append([row[' degree'], row[' title'], row[' email']])
        else:
            professor_dict[(firstname, surname)] = [row[' degree'], row[' title'], row[' email']]

# printing!
print {name:faculty_dict[name] for name in faculty_dict.keys()[:3]}, '\n'# print faculty_dict
print {name:professor_dict[name] for name in professor_dict.keys()[:3]}, '\n' # print professor_dict

# print sorted professor_dict
keysbylast = sorted(professor_dict, key = lambda name: name[1]) # sort keys by last name
for item in keysbylast[:3]: 
    print item, professor_dict[item]

'''note that using a dict comprehension {name:professor_dict[name] for name in keysbylast[:3]} yields the 
first three profs by last name but not necessarily in alphabetical order'''

