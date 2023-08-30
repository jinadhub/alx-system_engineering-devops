#!/usr/bin/env python3

import os

def create_dir(directory_name):
    if os.path.isdir(directory_name) != True:
        os.mkdir(directory_name)
    else:
        print(f"{directory_name} already exist!")


#os.mkdir("0x00-shell_basis")
#create_dir("0x00-shell_basis")


os.chdir("0x00-shell_basis")

def create_file(filename):
    if filename == "0-current_working_directory":
        with open(filename, "w") as fp:
            fp.write("#!/bin/bash\npwd\n")
    elif filename == "README.md":
        with open(filename, "w") as readme:
            readme.write("This is a readme file")



create_file("0-current_working_directory")
create_file("README.md")
    
