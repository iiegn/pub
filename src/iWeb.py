#!/usr/bin/env python

import sys,os
usage = "usage: %s searchText insertText_file [infile [outfile]]" % os.path.basename(sys.argv[0])

def init():

	stext = sys.argv[1]
	
	replaceTextFileIn = open(sys.argv[2],'r')
	replaceTextFileContent = replaceTextFileIn.readlines() 
	replaceTextFileIn.close()

	# print replaceTextFileContent

	input = sys.stdin
	output = sys.stdout
	if len(sys.argv) > 3:
		input = open(sys.argv[3])

	inputContent = input.readlines()
	input.close()

	if len(sys.argv) > 4:
		output = open(sys.argv[4], 'w')

	for s in inputContent:
		output.write(s.replace(stext, ''.join(replaceTextFileContent) + stext))

	output.close()

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print usage
		sys.exit(1)
	else:
		init()
