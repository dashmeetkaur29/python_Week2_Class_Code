#3.Write a Python program to display the current date and time.

'''
This program will display the current date and time by using the datetime library
'''

import datetime

def showDateTime():
    print("\nThe current date is - ", datetime.date.today()) #display current date
    time_st = datetime.datetime.now().strftime("%H:%M:%S")
    print("The current time is - ", time_st)    #display current time