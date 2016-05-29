import getopt
import sys

#help option
def helpmenu():
	print('Welcome to Code Snippet Manager!\n')
	print('-l       :list all code snippets\n-n name  :name of new code snippet\n-r name  :name of code snippet being retrieved')
	sys.exit()

#add new code snippet with name passed in argument
def add(name):
	filename = name + '.txt'
	file1 = open(filename, 'w')
	last = None
	last = str(raw_input())
	while last != '~':
		file1.write(last)
		file1.write('\n')
		last = str(raw_input())
	file1.close()
	file2 = open('master.txt', 'a')
	file2.write(name + '\n')
	file2.close()
	sys.exit()

def retrieve(name):
	filename = name + '.txt'
	file1 = open(filename, 'r')
	for line in file1:
		print(line)
	file1.close()
	sys.exit()

def listall():
	masterfile = open('master.txt', 'r')
	for line in masterfile:
		print(line)
	masterfile.close()
	sys.exit()

def main():
	try:
		#options
		opts, args = getopt.getopt(sys.argv[1:], 'hln:r:', ['name=', 'retrieve='])
	except getopt.GetoptError:
		print("invalid option")
		helpmenu()
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			helpmenu()
                elif opt == '-l':
                        listall()
		elif opt in ('-n','--name'):
			add(arg)
		elif opt in ('-r','--retrieve'):
			retrieve(arg)
		else:
			sys.exit()

if __name__ == '__main__':
	main()
