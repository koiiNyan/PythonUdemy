# Write a script that counts the number of .py files contained inside subdirs and all its sub-directories.

import glob

def files_counter(path):
    file_counter = len(glob.glob(path, recursive=True))
    return file_counter

print(files_counter('subdirs/**/*.py'))

# If recursive is true, the pattern “**” will match any files and zero or more directories and subdirectories.
