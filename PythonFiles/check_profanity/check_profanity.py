import urllib

''' The program reads the specefic file and from a google wdylike service
    tells us if the text in the file has any curse words or not '''
def read_file():
    content = open("C:/Users/DIPANSH KHANDELWAL/Desktop/Python Codes/PythonFiles/check_profanity/check_profanity.txt")
    text = content.read()
    print (text)
    content.close()
    check_profanity(text)

def check_profanity(text_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_check)
    output = connection.read()
    print("Response :- "+output)
    connection.close()

read_file()
