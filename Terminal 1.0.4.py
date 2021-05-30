# Copyright (c) JaylyDev.  All rights reserved.
# Copyrights licensed under the MIT License.
# See the accompanying LICENSE (https://github.com/JaylyDev/JaylyTerminal/blob/release-1.1/LICENSE) file for terms.
#functions import
import os
import inspect
import sys
import math
import locale
import logging
import time
import zipfile
import codecs
from distutils.dir_util import copy_tree
from distutils.dir_util import remove_tree
from distutils import log

#program setup
locale.setlocale(locale.LC_ALL, 'en_US') #Decimals on numbers
current_path = inspect.getfile(inspect.currentframe()) #Current directory
current_filename = os.path.basename(__file__)
current_path = str(current_path).replace("\\" + str(current_filename), "")
version = [1, 0, 4, 1] #Program version
version_code = version
version = str(version).replace(",", ".")
version = str(version).replace(" ", "")
version = str(version).replace("]", "")
version = str(version).replace("[", "")
code = "4e41" #NA
cmd = ""

#define commands
def jt_code():
    if code == "4e41":
        print("NA")
    elif code == "68656c70":
        jt_help()
    elif code == "627265616b":
        jt_exit()
    elif code == "6469726c697374":
        jt_dirlist()
    elif code == "6d6f7665":
        jt_dirmove()
    elif code == "64697273697a65":
        jt_dirsize()
    elif code == "646972636f7079":
        jt_dircopy()
    elif code == "64697264656c657465":
        jt_dirdelete()
    elif code == "74696d6572":
        jt_stopwatch()
    elif code == "7a6970646972":
        jt_zipdir()
    elif code == "646972736561726368":
        jt_dirsearch()
    elif code == "66696c6572656164":
        jt_readfile()
    elif code == "66696c65637265617465":
        jt_create_file()
    elif code == "66696c6564656c657465":
        jt_delete_file()
    elif code == "756e6b6e6f776e434d44":
        print("Error: The command \"" + cmd + "\" is not recognized in command list.")
    else:
        print("Error: Terminal unable to detect code request. Code: " + str(code))

def jt_help():
    global cmd_input
    try:
        if cmd_input[1] == "/ver":
            jt_program_version()
        #elif cmd_input[1] == "/cl":
        #    jt_program_changelog(version_code)
        else:
            jt_help_text()
    except:
        jt_help_text()

def jt_program_changelog(version_cl):
    #code here soon kbye
    if version_cl == [1, 0, 0]:
        print(version_cl)

def jt_help_text():
    print("""
TOPIC
    JaylyTerminal help system

DESCRIPTION
    Displays help about JaylyTerminal commands and concepts.

COMMANDS
    MODULE: JaylyTerminal Support
        exit - Exit Terminal
        help - JaylyTerminal help system
        move - Change the directory you want to execute commands on
    MODULE: Directory Handling
        dirsize - Check the size of the current directory
        dircopy - Copy a directory from one to other
        dirlist - List files and folders name current directory
        dirdelete - Delete current directory (VERY DANGEROUS)
        dirsearch - Search directories through a keyword
    MODULE: File Handling
        fileread - Read a file
        filedelete - Delete a file
        filecreate - Create a file
    MODULE: Data Compression
        zipdir - Archive current directory using ZIP file format
    MODULE: Time
        stopwatch - A stopwatch that counts the time.
""")

def jt_program_version():
    jt_ver = version_code[0]
    jt_revision_ver = version_code[1]
    jt_maintenance_ver = version_code[2]
    jt_commit_ver = version_code[3]
    print("Terminal Version: " + str(jt_ver))
    print("Revision Version: " + str(jt_revision_ver))
    print("Maintenance Version: " + str(jt_maintenance_ver))
    print("Commit Version: " + str(jt_commit_ver))

def jt_exit():
    print("Closing program.")
    sys.exit()

def jt_dirlist():
    listdir_path = str(current_path)
    try:
        dirs = os.listdir(str(listdir_path))
        # This would print all the files and directories
        for file in dirs:
            print(file)
    except Exception as Error:
        print(str(Error))

def jt_dirmove():
    global cmd_input
    global current_path
    try:
        request_path = cmd_input[1:]
        jt_list_symbols_remove(request_path)
        global var_output
        request_path = var_output
        if os.path.exists(os.path.join(os.getcwd(), str(request_path))) == True:
            current_path = str(request_path)
        else:
            print("Error: Directory \"" + str(request_path) + "\" not found.")
            current_path = inspect.getfile(inspect.currentframe()) #Current directory
            current_filename = os.path.basename(__file__)
            current_path = str(current_path).replace("\\" + str(current_filename), "")
    except Exception as Error:
        print("Error: " + str(Error))
        print("Usage: move [Directory]") 

def jt_dirmove_help():
    print("Usage: \"dirmove\" + directory target")

def jt_dirsize_ext(current_path):
    #Units
    petabyte = 1000000000000000
    terabyte = 1000000000000
    gigabyte = 1000000000
    megabyte = 1000000
    kilobyte = 1000
    #program 
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

def jt_dirsize():
    global current_path
    global cmd_input
    try:
        if cmd_input[1] == "/loop":
            loop = True
            if cmd_input[2] == "/time":
                print(cmd_input[3])
            else:
                pass
        else:
            loop = False
    except:
        loop = False
    try:
        if loop == True:
            while True: #Calculate directory size
                jt_dirsize_ext(current_path)
        elif loop == False:
            jt_dirsize_ext(current_path)
    except Exception as Error:
        print("Error: " + str(Error))

def jt_dircopy():
    global cmd_input
    fromDirectory = current_path
    try:
        toDirectory = cmd_input[1:]
        jt_dircopy_exe(fromDirectory, toDirectory)
    except:
        print("Usage: dircopy [Directory you want to copy to]")
    #fromDirectory = str(fromDirectory).replace("\\", "\\\\")
    #toDirectory = str(toDirectory).replace("\\", "\\\\")
    #distutils is okay

def jt_dircopy_exe(fromDirectory, toDirectory):
    try:
        print(log.set_verbosity(log.INFO))
        print(log.set_threshold(log.INFO))
        copy_tree(fromDirectory, toDirectory)
    except Exception as Error:
        print("Error: " + str(Error))

def jt_dirdelete():
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

def jt_stopwatch():
    one_sec_ago = time.perf_counter()
    now = time.perf_counter()
    start_time = time.perf_counter()
    stopwatch = time.perf_counter()
    while True:
        now = time.perf_counter()
        time_diff = stopwatch - start_time
        time_diff_print = round(time_diff, 1)
        time_difference = now - one_sec_ago
        stopwatch = time.perf_counter()
        if time_difference >= 0.1:
            print("Time: " + str(time_diff_print) + "s")
            one_sec_ago = time.perf_counter()
        else:
            pass

def jt_zipdir():
    #This command asks user to input file name and source directory
    #after they input the directory, it executes function jt_zipdir_execution
    global cmd
    global current_path
    cmd = cmd.split()
    try:
        command = cmd[0]
        source_dir = current_path
        output_filename = cmd[1:]
        try:
            #if os.path.exists(source_dir) and (os.path.isfile(output_filename) or os.path.exists(output_filename)):
            jt_zipdir_execution(output_filename, source_dir)
        except Exception as Error:
            print("Error: " + str(Error))
            print("Usage: zipdir [filename (output)]")
    except Exception as Error:
        print("Error: " + str(Error))
        print("Usage: zipdir [filename (output)]")

def jt_zipdir_execution(output_filename, source_dir): # Credit to https://stackoverflow.com/a/17080988
    relroot = os.path.abspath(os.path.join(source_dir, os.pardir))
    with zipfile.ZipFile(output_filename, "w", zipfile.ZIP_DEFLATED) as zip:
        for root, dirs, files in os.walk(source_dir):
            # add directory (needed for empty dirs)
            zip.write(root, os.path.relpath(root, relroot))
            for file in files:
                filename = os.path.join(root, file)
                if os.path.isfile(filename): # regular files only
                    arcname = os.path.join(os.path.relpath(root, relroot), file)
                    zip.write(filename, arcname)
    print("Created a ZIP file.")

def jt_delete_file():
    global cmd_input
    try:
        filepath = cmd_input[1:]
        jt_delete_file_exe(filepath)
    except Exception as Error:
        print("Error: " + str(Error))
        print("Usage: delfile [File location]")

def jt_create_file():
    global cmd_input
    try:
        file = cmd_input[1]
        content = cmd_input[2]
        jt_create_file_exe(file, content)
    except Exception as Error:
        print("Error: " + str(Error))
        print("Usage: writefile [File location] [content]")

def jt_readfile():
    global cmd_input
    try:
        filepath = cmd_input[1]
        encode = cmd_input[2]
        jt_readfile_exe(filepath, encode)
    except Exception as Error:
        print("Error: " + str(Error))
        print("Usage: readfile [File location] [Encoding format]")

def jt_delete_file_exe(filepath): #This command is not available for 1.1.1.0
    if os.path.exists(filepath):
        os.remove(filepath)
    else:
        print("The file does not exist")

def jt_create_file_exe(filepath, content):
    jt_file = open(str(filepath), "a")
    jt_file.write(str(content))
    jt_file.close()

def jt_readfile_exe(file, encode):
    with codecs.open(file, encoding = encode) as file:
        lines = file.read()
        try:
            print(lines)
        except Exception as Error:
            print(str(Error))

def jt_dirsearch():
    global cmd_input
    global current_path
    try:
        keyword = cmd_input[1]
        try:
            start_dir = cmd_input[2]
        except:
            start_dir = current_path
        jt_dirsearch_exe(keyword, start_dir)
    except Exception as Error:
        print("Error: " + str(Error))
        print("Usage: dirsearch [Directory name] [Start directory (Default: Current path)]")

def jt_dirsearch_exe(keyword, start_dir):
    for dirpath, dirnames, filenames in os.walk(start_dir):
        for pathname in dirnames:
            if pathname == keyword:
                pathname = os.path.join(pathname)
                print("Found folder \"" + pathname + "\". Location: " + dirpath + "\\" + pathname)
#                f.write("Found folder \"" + pathname + "\". Location: " + dirpath + "\\" + pathname + "\n")
#                f.close()
#                f = open("demofile2.txt", "a")
            else:
                continue

# jt_filesearch() and jt_filesearch_exe() are not available before version 1.1.2.0
def jt_filesearch():
    global cmd_input
    try:
        keyword = cmd_input[1]
    except Exception as Error:
        print("Error: " + str(Error))
        print("Usage: dirsearch [Directory name] [Start directory (Default: C:\\)]")
    try:
        start_dir = cmd_input[2]
    except:
        pass

def jt_filesearch_exe(keyword, start_dir):
    for dirpath, dirnames, filenames in os.walk(start):
        for pathname in dirnames:
            if pathname == keyword:
                pathname = os.path.join(pathname)
                print("Found folder \"" + pathname + "\". Location: " + dirpath + "\\" + pathname)
#                f.write("Found folder \"" + pathname + "\". Location: " + dirpath + "\\" + pathname + "\n")
#                f.close()
#                f = open("demofile2.txt", "a")
            else:
                continue

def jt_list_symbols_remove(variable):
    global var_output
    variable = str(variable).replace("[", "")
    variable = str(variable).replace("]", "")
    variable = str(variable).replace(",", "")
    variable = str(variable).replace("'", "")
    variable = str(variable).replace("\\\\", "\\")
    var_output = variable

#Program start running
print("JaylyDirectory [Version " + str(version) + "]")
print("""(c) JaylyDev. All rights reserved.
""")
while True:
    cmd = input(str(current_path) + ">") #input
    cmd_input = cmd.split()
    try:
        command = cmd_input[0]
        if command.lower() == "help":
            code = "68656c70"
        elif command.lower() == "exit":
            code = "627265616b"
        elif command.lower() == "dirlist":
            code = "6469726c697374"
        elif command.lower() == "dircopy":
            code = "646972636f7079"
        elif command.lower() == "dirdelete":
            code = "64697264656c657465"
        elif command.lower() == "zipdir":
            code = "7a6970646972"
        elif command.lower() == "stopwatch":
            code = "74696d6572"
        elif command.lower() == "move":
            code = "6d6f7665"
        elif command.lower() == "dirsize":
            code = "64697273697a65"
        elif command.lower() == "delfile":
            code = "64656c66696c65"
        elif command.lower() == "dirsearch":
            code = "646972736561726368"
        elif command.lower() == "fileread":
            code = "66696c6572656164"
        elif command.lower() == "filecreate":
            code = "66696c65637265617465"
        elif command.lower() == "filedelete":
            code = "66696c6564656c657465"
        else:
            code = "756e6b6e6f776e434d44" #Hex to text: unknownCMD
            
        try: #redirect to my_function "code"
            jt_code()
        except Exception as Error:
            print("Error: " + str(Error))
    except:
        pass
