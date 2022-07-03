#! /bin/python
import time
import os
number = int(input("enter how many time you want ip to change (enter 0 for non limit):"))
if number == 0 :
    i = 0
    while True:
        print(i)
        time.sleep(10)
        os.system("sudo service tor restart")
        i+=1
else :
    i = 0
    while number > 0 :
        print(i)
        time.sleep(30)
        os.system("sudo service tor restart")
        number -= 1
        i+=1
        print("done!")