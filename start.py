#! /bin/python3
import os

app=input("enter the name of module or app u want to use : ")
os.system("sudo service tor reload")
os.system(f"proxychains {app}")