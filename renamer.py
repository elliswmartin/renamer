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

    # do not rename if file names are the same 
    if file == new_name[index]:
        print(file + " not renamed to " + new_name[index] + "\nOriginal and new filenames are the same.")
        shutil.move(cwd + file, nwd + file)
   
    # do not rename if new filename already exists in subfolder
    elif new_name[index] in os.listdir(nwd):
        print(file + " not renamed to " + new_name[index] + ".\nNew filename already exists in 'done' folder")
    
    # all clear to rename
    else:
        try: 
            shutil.copy(cwd + file, nwd + new_name[index])
            print("File renamed successfully.")
            os.remove(file) # remove file once renamed and moved 
        except: 
            print("Error occurred while renaming file.")