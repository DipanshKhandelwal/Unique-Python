import os

#This program finds all the files in a directory whose address we provide and prints it.
def get_files():
    file_list = os.listdir(r"C:\Users\DIPANSH KHANDELWAL\Desktop")
    print (file_list)

get_files()
