import os

'''program read all the files in the given directory prints all the file
name present and even change all the files name removing any number
present in the file name'''

def rename_files():
    file_list = os.listdir(r"C:\Users\DIPANSH KHANDELWAL\Desktop\Python Codes\RenameFiles\photos")
    print (file_list)
    os.chdir("C:\Users\DIPANSH KHANDELWAL\Desktop\Python Codes\RenameFiles\photos")
    for file_name in file_list:
        os.rename(file_name , file_name.translate(None,"123456789"))
        print "file " + file_name + " changed to " + file_name.translate(None,"123456789")
rename_files()
