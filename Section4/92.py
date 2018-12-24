# Write a script that counts and prints out the number of .py files in the folder.

import glob

def files_counter(dir,file_type):
    file_counter = len(glob.glob1(dir,file_type))
    return file_counter

print(files_counter('files','*.py'))

# Glob is a standard Python library that finds pathnames matching
# a specified pattern. glob1 takes a directory name as first argument
# and a pattern.
