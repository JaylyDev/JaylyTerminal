# This file is a module extension orginially created for JaylyConsole
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
from distutils.dir_util import remove_tree
from distutils import log

#program setup
locale.setlocale(locale.LC_ALL, 'en_US') #Decimals on numbers
current_path = inspect.getfile(inspect.currentframe()) #Current directory
current_filename = os.path.basename(__file__)
current_path = str(current_path).replace("\\" + str(current_filename), "")
version = [1, 1, 0] #Program version
version_code = version
version = str(version).replace(",", ".")
version = str(version).replace(" ", "")
version = str(version).replace("]", "")
version = str(version).replace("[", "")
code = "4e41" #NA
cmd = ""

#define commands
def jd_code():
    if code == "4e41":
        print("NA")
    elif code == "68656c70":
        jd_help()
    elif code == "627265616b":
        jd_break()
    elif code == "6469726c697374":
        jd_dirlist()
    elif code == "68656c70202f76657273696f6e":
        jd_program_version()
    elif code == "6469726d6f7665":
        jd_dirmove()
    elif code == "64697273697a65":
        jd_dirsize()
    elif code == "646972636f7079":
        jd_dircopy()
    elif code == "64697264656c657465":
        jd_dirdelete()
    elif code == "756e6b6e6f776e434d44":
        print("Error: The command \"" + cmd + "\" is not recognized in command list.")
    else:
        print("Error: Terminal unable to detect code request. Code: " + str(code))

def jd_help():
    print("""
TOPIC
    JaylyDirectory Terminal help system

DESCRIPTION
    Displays help about JaylyConsole Terminal cmdlets and concepts.

COMMANDS
    MODULE: JaylyConsole Terminal Support
        break - Exit Terminal
        help - JaylyDirectory Terminal help system
    MODULE: Directory Handling
        dirmove - Execute commands on the specific directory
        dirsize - Check the size of the current directory
        dircopy - Copy a directory from one to other
        dirlist - List files and folders name current directory
        dirdelete - Delete current directory (VERY DANGEROUS)
""")

def jd_break():
    print("Closing program.")
    sys.exit()

def jd_dirlist():
    listdir_path = str(current_path)
    try:
        dirs = os.listdir(str(listdir_path))
        # This would print all the files and directories
        for file in dirs:
            print(file)
    except Exception as Error:
        print(str(Error))

def jd_program_version():
    jd_ver = version_code[0]
    jd_revision_ver = version_code[1]
    jd_commit_ver = version_code[2]
    print("Terminal Version: " + str(jd_ver))
    print("Revision: " + str(jd_revision_ver))
    print("Commit Version: " + str(jd_commit_ver))

def jd_dirmove():
    global current_path
    request_path = str(cmd).replace("dirmove ", "")
    if os.path.exists(os.path.join(os.getcwd(), str(request_path))) == True:
        current_path = str(request_path)
    else:
        print("Error: Directory " + str(request_path) + " not found.")
        current_path = inspect.getfile(inspect.currentframe()) #Current directory
        current_path = str(current_path).replace("\\directory.py", "")  

def jd_dirmove_help():
    print("Usage: \"dirmove\" + directory target")

def jd_dirsize():
    global current_path
    #Units
    petabyte = 1000000000000000
    terabyte = 1000000000000
    gigabyte = 1000000000
    megabyte = 1000000
    kilobyte = 1000
    try:
        if "/loop" in cmd:
            loop = True
        else:
            loop = False
            
        if loop == True:
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
        elif loop == False:
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

def jd_dircopy():
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

def jd_dirdelete():
    global current_path
    print("You have requested to delete directory \"" + str(current_path) + "\"")
    dirdelete_alert = input("Are you sure? (yes/no): ").lower()
    if dirdelete_alert == "yes":
        try:
            print(log.set_verbosity(log.INFO))
            print(log.set_threshold(log.INFO))
            remove_tree(current_path)
            #Returning back to file origin
            current_path = inspect.getfile(inspect.currentframe()) #Current directory
            current_filename = os.path.basename(__file__)
            current_path = str(current_path).replace("\\" + str(current_filename), "")
        except Exception as Error:
            print("Error: " + str(Error))
    elif dirdelete_alert == "no":
        print("Decline request.")
    else:
        print("Invalid input, decline request.")

#Program start running
print("JaylyDirectory [Version " + str(version) + "]")
print("""(c) JaylyDev. All rights reserved.
""")
while True:
    cmd = input(str(current_path) + ">") #input
    if cmd.lower() == "help":
        code = "68656c70"
    elif cmd.lower() == "break":
        code = "627265616b"
    elif cmd.lower() == "dirlist":
        code = "6469726c697374"
    elif cmd.lower() == "help /version":
        code = "68656c70202f76657273696f6e"
    elif cmd.lower() == "dircopy":
        code = "646972636f7079"
    elif cmd.lower() == "dirdelete":
        code = "64697264656c657465"
    elif "dirmove" in cmd.lower():
        code = "6469726d6f7665"
    elif "dirsize" in cmd.lower():
        code = "64697273697a65"
    else:
        code = "756e6b6e6f776e434d44" #Hex to text: unknownCMD
    
    try: #redirect to my_function "code"
        jd_code()
    except Exception as Error:
        print("Error: " + str(Error))
