# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

# a) solution
date_format = '%m-%d-%Y' # create date format to match given start/stop format

start = datetime.strptime(date_start, date_format) # change string to datetime object
stop = datetime.strptime(date_stop, date_format)

dif = stop - start
print dif

####b)  
date_start = '12312013'  
date_stop = '05282015' 

# b) solution

date_format_b = '%m%d%Y'

start = datetime.strptime(date_start, date_format_b)
stop = datetime.strptime(date_stop, date_format_b)

difb = stop - start
print difb 

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

# c) solution

date_format_c = '%d-%b-%Y'

start = datetime.strptime(date_start, date_format_c)
stop = datetime.strptime(date_stop, date_format_c)

difc = stop - start
print difc