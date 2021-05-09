# This file is an extension created for JaylyConsole
# Copyright (c) JaylyDev.  All rights reserved.
# Copyrights licensed under the MIT License.
# See the accompanying LICENSE (https://github.com/JaylyDev/JaylyConsole/blob/beta-1.3/LICENSE) file for terms.
#functions import
import os
import inspect
import sys
import math
import locale
import logging
from distutils.dir_util import copy_tree
from distutils import log

#program setup
locale.setlocale(locale.LC_ALL, 'en_US') #Decimals on numbers
current_path = inspect.getfile(inspect.currentframe()) #Current directory
current_path = str(current_path).replace("\\directory.py", "")
#For dirsize
petabyte = 1000000000000000
terabyte = 1000000000000
gigabyte = 1000000000
megabyte = 1000000
kilobyte = 1000

#Porgram start running
print("""JaylyDirectory [Version 1.0.48]
(c) JaylyDev. All rights reserved.
""")
success = False
loop = False
copy = False
while True:
    cmd = input(str(current_path) + ">").lower()  # To get size of current directory
    #Command checking
    if "dirmove " in cmd: #Directory move
        cmd = str(cmd).replace("dirmove ", "")
        if os.path.exists(os.path.join(os.getcwd(), str(cmd))) == True:
            current_path = cmd
            success = False
        else:
            print("Error: Directory " + str(cmd) + " not found.")
            current_path = inspect.getfile(inspect.currentframe()) #Current directory
            current_path = str(current_path).replace("\\directory.py", "")
            
    elif "dirsize" in cmd: #Check directory size command
        success = True
        loop = False
        if "/loop" in cmd:
            cmd = str(cmd).replace("/loop", "")
            loop = True
            success = True
    elif cmd == "break": # Shut down the program
        sys.exit()
    elif cmd == "dircopy":
        copy = True
    elif cmd == "help":
        print("""
TOPIC
    JaylyConsole Terminal help system

DESCRIPTION
    Displays help about JaylyConsole Terminal cmdlets and concepts.

COMMANDS
    MODULE: JaylyConsole Terminal Support
        break - Exit Terminal
        help - JaylyConsole Terminal help system
    MODULE: Directory Handling
        dirmove - Execute commands on the specific directory
        dirsize - Check the size of the current directory
        dircopy - Copy a directory from one to other
        dirlist - List current directory
""")
    elif "dirlist" in cmd:
        listdir_path = str(current_path)
        try:
            dirs = os.listdir(str(listdir_path))
            # This would print all the files and directories
            for file in dirs:
                print(file)
        except Exception as Error:
            print(str(Error))
    else:
        print("Error occured")
        success = False
        
    #Executes commands for dirsize
    if success == True:
        try:
            if(loop == True):
                while True: #Calculate directory size
                    total_size = 0
                    bytes_size = 0
                    try:
                        for path, dirs, files in os.walk(str(current_path)):
                            for f in files:
                                fp = os.path.join(path, f)
                                total_size += os.path.getsize(fp)
                                bytes_size = "{:,}".format(total_size)
                    except Exception as Error:
                        print("Error: " + str(Error))
                    #Converts bytes to suitible values
                    if total_size >= petabyte:
                        total_size = total_size / petabyte #Get PB value
                        total_size = round(total_size, 2) #Round to 2 d.p
                        total_size = str(total_size) + " petabytes"
                    elif total_size >= terabyte: 
                        total_size = total_size / terabyte #Get TB value
                        total_size = round(total_size, 2) #Round to 2 d.p.
                        total_size = str(total_size) + " terabytes"
                    elif total_size >= gigabyte:
                        total_size = total_size / gigabyte #Get GB value
                        total_size = round(total_size, 2) #Round to 2 d.p.
                        total_size = str(total_size) + " gigabytes"
                    elif total_size >= megabyte: 
                        total_size = total_size / megabyte #Get MB value
                        total_size = round(total_size, 2) #Round to 2 d.p.                        
                        total_size = str(total_size) + " megabytes"
                    elif total_size >= kilobyte: 
                        total_size = total_size / kilobyte #Get KB value
                        total_size = round(total_size, 2) #Round to 2 d.p.             
                        total_size = str(total_size) + " kilobytes"
                    else:                       
                        total_size = str(total_size) + " bytes"
                        
                    print("Directory size: " + str(total_size) + " (" + str(bytes_size) + " bytes)")
            elif(loop == False):
                total_size = 0
                bytes_size = 0
                try:
                    for path, dirs, files in os.walk(str(current_path)):
                        for f in files:
                            fp = os.path.join(path, f)
                            total_size += os.path.getsize(fp)
                            bytes_size = "{:,}".format(total_size)
                except Exception as Error:
                    print("Error: " + str(Error))
            #Converts bytes to suitible values
                if total_size >= petabyte:
                    total_size = total_size / petabyte #Get PB value
                    total_size = round(total_size, 2) #Round to 2 d.p.                    
                    total_size = str(total_size) + " petabytes"
                elif total_size >= terabyte: 
                    total_size = total_size / terabyte #Get TB value
                    total_size = round(total_size, 2) #Round to 2 d.p.                    
                    total_size = str(total_size) + " terabytes"
                elif total_size >= gigabyte:
                    total_size = total_size / gigabyte #Get GB value
                    total_size = round(total_size, 2) #Round to 2 d.p.                    
                    total_size = str(total_size) + " gigabytes"
                elif total_size >= megabyte: 
                    total_size = total_size / megabyte #Get MB value
                    total_size = round(total_size, 2) #Round to 2 d.p.
                    total_size = str(total_size) + " megabytes"
                elif total_size >= kilobyte: 
                    total_size = total_size / kilobyte #Get KB value
                    total_size = round(total_size, 2) #Round to 2 d.p. 
                    total_size = str(total_size) + " kilobytes"
                else:
                    total_size = str(total_size) + " bytes"
                print("Directory size: " + str(total_size) + " (" + str(bytes_size) + " bytes)")
        except Exception as Error:
            print("Error: " + str(Error))
    if success == False:
        pass
    #copy module
    if copy == True:
        fromDirectory = input("From directory: ")
        toDirectory = input("To directory: ")
        #fromDirectory = str(fromDirectory).replace("\\", "\\\\")
        #toDirectory = str(toDirectory).replace("\\", "\\\\")
        #distutils is okay
        try:
            print(log.set_verbosity(log.INFO))
            print(log.set_threshold(log.INFO))
            copy_tree(fromDirectory, toDirectory)
        except Exception as Error:
            print("Error: " + str(Error))
