import os, re, csv, shutil

os.chdir("/Users/ellis/Desktop/rename") 
cwd = os.getcwd() + "/"
nwd = cwd + "done/" # subdirectory to move renamed files into

file = open('rename.csv')
file = csv.reader(file)

old_name = []
new_name = []

# create lists of old and new names from rename.csv
for line in file:
    old_name.append(line[0]) 
    new_name.append(line[1])

# create new subdirectory if does not already exist 
if os.path.exists(nwd) == False: 
    os.makedirs(nwd)

# loop through files in old_name list to rename      
for file in old_name:
    index = old_name.index(file)

    # if file has not been renamed 
    if file != new_name[index]:
        try:
            shutil.copy(cwd + file, nwd + new_name[index])
            print("File copied successfully.")
        # error: source and destination are same - TODO these don't work rn 
        except shutil.SameFileError:
            print("File already exists in destination folder.")
        # error: any permission issue
        except PermissionError:
            print("Permission denied.")
        # any other errors
        except:
            print("Error occurred while copying file.")

        os.chdir(nwd) # move to subdirectory
        os.chdir(cwd) # return to main directory 
        os.remove(file) # remove file once renamed and moved 
    else:
        print(file + " has already been renamed.")