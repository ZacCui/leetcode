#!/usr/local/bin/python3

import sys
import os

if len(sys.argv) != 2:
	print('Usage : ./create_dir "<questionname>"')
	exit()

name_str = sys.argv[1].replace('.', '')
num = name_str.split(' ')[0]
dirname = '_'.join(str(name_str).lower().split(' '))
path = '{}/{}'.format(os.getcwd(), dirname)

try:  
    os.mkdir(path)
except OSError:  
    print ("Creation of the directory %s failed" % path)
else:  
    print ("Successfully created the directory %s " % path)

languages = ['py', 'java', 'cpp']

for lan in languages:	
	with open('{}/{}.{}'.format(path, num, lan), 'w+') as f:
		if lan == 'py': f.write('#!/usr/local/bin/python3')
		print ("Successfully created the file %s " % '{}/{}.py'.format(path, num))
