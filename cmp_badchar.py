#!/usr/bin/python3
import sys
if (len(sys.argv) != 2):
	print ('Usage: python cmp_badchar.py <FILE_DIR>')
	sys.exit()

data = open(sys.argv[1],'r').read()
for i in range (0x01, 0xFF+1):
	string = format(i,'02x')
	result = data[2*i-2:2*i]
	if (string != result):
		print ('Bad Char: '+ string +" --> "+result)
