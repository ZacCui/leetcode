#!/usr/local/bin/python3

import sys
import os
import datetime

#config
author = os.environ['FULL_NAME'] if os.environ.get('FULL_NAME') else 'Unknown'
time = str(datetime.datetime.now()).split('.')[0]
languages = ['py']

def search_question(num):
	for file_name in os.listdir():
		if file_name.split('_')[0] == num:
			return file_name
	print('Question {} does not exist'.format(num))
	exit()

def create_dir(path):
	if not os.path.exists(path):
		try:  
			os.mkdir(path)
		except OSError:  
			print ("Creation of the directory %s failed" % path)
			exit()
		else:  
			print ("Successfully created the directory %s " % path)
	else:
		print ("Directory %s exists" % path)

def create_file(path):
	file_author = '_'.join(author.lower().split(' '))
	num = path.split('/')[-1].split('_')[0]
	for lan in languages:	
		file_name = '{}/{}_{}.{}'.format(path, file_author, num, lan)
		if not os.path.exists(file_name):
			with open(file_name, 'w+') as f:
				if lan == 'py': 
					f.write('#!/usr/local/bin/python3\n')
					f.write("\'\'\'\n\tAuthor: {}\n\tCreated Date: {}\n\'\'\'".format(author, time))
				else:
					f.write("/*\n\tAuthor: {}\n\tCreated Date: {}\n*/".format(author, time))
				print ("Successfully created the file %s " % file_name)
		else:
			print ("File %s exists" % file_name)


if len(sys.argv) != 2:
	print('Usage : python3 create_dir "<question_name>" | <question_number>')
	exit()

if sys.argv[1].isdigit():
	path = '{}/{}'.format(os.getcwd(), search_question(str(sys.argv[1])))
	create_file(path)
else:
	name_str = sys.argv[1].replace('.', '')
	dirname = '_'.join(str(name_str).lower().split(' '))
	path = '{}/{}'.format(os.getcwd(), dirname)
	create_dir(path)
	create_file(path)
