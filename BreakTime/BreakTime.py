import time
import webbrowser

'''This program reminds you to take a small break after working
on your pc for a fixed time interval ( here 30 minutes ) and opens a link in any
webbrowser to any of your favourite website'''

break_count = 0
print("Your break time program started on " + time.ctime())
while(True):
    time.sleep(1800)
    break_count += 1
    print("This is your break number " + str(break_count) + " at :- " + time.ctime())
    webbrowser.open("https://www.youtube.com/")   
