import os

#This program finds all the files in a directory whose address we provide and prints it.
def get_files():
	directory = os.path.join('C:\\Users\\%s\\Desktop' %os.getlogin())
	file_list = os.listdir(directory)
	print (file_list)

def main():
	get_files()

if __name__ == '__main__':
	main()