# renamer
Python script to bulk rename files while maintaining user control of names on the file level. 

## How It Works
This script uses _____

## Usage 

1. This script ships assuming the following folder structure. You are welcome to modify this for your needs within the /renamer.py script.

        ├── Desktop
        │   ├── rename
        │   │   ├── done      

2. Add your image files to be processed into the "/Desktop/rename" folder. If you do not have a done subfolder, one will be created automatically during processing. 

3. Add file names to a spreadsheet with Column A containing only the original file names (not column title) and Column B similarly containing the new file names. The length of each column must match. Save or download spreadsheet as "rename.csv". 

![CSV Example](csv_example.png)

4. Open Terminal and run the rename script. Images will appear in the "~/Desktop/rename/done" folder when finished.

## Background
I developed this script to handle bulk renaming while at Letterform Archive in San Francisco, CA. 
