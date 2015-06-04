import os
import sys

rootdir = "."
exist = {}
totalLOC = 0;

#parse command line arguments for extensions and path
def parseArguments():
	global exist
	global rootdir
	for i in range(1, len(sys.argv)):

		if sys.argv[i] == "--help":
			showHelp()
			i+=1
			sys.exit(0)

		if sys.argv[i] == '--ext':

			if i+1 >= len(sys.argv):
				print "Missing extension parameters.  Type --help for list of commands."
				sys.exit(0)

			if not sys.argv[i+1].startswith('.'):
				print "Invalid file extension format."
				sys.exit(0)

			while not sys.argv[i+1].startswith('--'):
				i+=1
				exist[sys.argv[i]] = 1
				if i+1 >= len(sys.argv):
					break

		if sys.argv[i] == '--path':

			if i+1 >= len(sys.argv):
				print "Missing path parameters.  Type --help for list of commands."
				sys.exit(0)

			i += 1
			rootdir = sys.argv[i]

			if not os.path.exists(rootdir):
				print "Cannot find path to directory."
				sys.exit(0)

#display the commands
def showHelp():
	print "Available commands:"
	print "--ext arg1 arg2...argn"
	print "arg must be in the format of .ext, where ext is the extension of the file you want to check."
	print "--path pathToDirectory"
	print "By default, the program will calculate lines of code for every file starting from the current directory."

#count files with user specified extensions
def countExtension():
	global totalLOC
	for root, subFolders, files in os.walk(rootdir):
 		for file in files:
			fileName, fileExtension = os.path.splitext(file)
			if fileExtension in exist:
	 	    		with open(os.path.join(root, file), 'r') as fin:			
					totalLOC += sum(1 for line in fin)	


#count lines regardless of file type
def countAll():
	global totalLOC
	for root, subFolders, files in os.walk(rootdir):
	 	for file in files:
			totalLOC += sum(1 for line in open(os.path.join(root, file), 'r'))


def main():
	parseArguments()

	if exist:
 		countExtension()
 	else:
 		countAll()

	print totalLOC

if __name__ == "__main__":
	main()