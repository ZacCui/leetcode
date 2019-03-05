#!/usr/local/bin/python3

import sys
import os
import datetime

if len(sys.argv) != 2:
	print('Usage : ./create_dir "<questionname>"')
	exit()

author = os.environ['FULL_NAME'] if os.environ.get('FULL_NAME') else 'Unknown'
time = str(datetime.datetime.now()).split('.')[0]
name_str = sys.argv[1].replace('.', '')
num = name_str.split(' ')[0]
dirname = '_'.join(str(name_str).lower().split(' '))
path = '{}/{}'.format(os.getcwd(), dirname)

try:  
    os.mkdir(path)
except OSError:  
    print ("Creation of the directory %s failed" % path)
    exit()
else:  
    print ("Successfully created the directory %s " % path)

languages = ['py', 'java', 'cpp']

for lan in languages:	
	with open('{}/{}.{}'.format(path, num, lan), 'w+') as f:
		if lan == 'py': 
			f.write('#!/usr/local/bin/python3\n')
			f.write("\'\'\'\n\tAuthor: {}\n\tCreated Date: {}\n\'\'\'".format(author, time))
		else:
			f.write("/*\n\tAuthor: {}\n\tCreated Date: {}\n*/".format(author, time))
		print ("Successfully created the file %s " % '{}/{}.{}'.format(path, num, lan))
