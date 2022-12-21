# renamer
Python script to bulk rename files while maintaining user control of names on the file level. 

## How It Works
This script creates two lists from a csv file stored in the rename folder, one list of the original (current) names and one list of the new names. The script iterates through the old_names list to copy the files into the subfolder, renaming with the new_names list as it does. The original files are deleted after the files are successfully moved.  

## Usage (Mac only)

1. This script ships assuming the following folder structure. You are welcome to modify this for your needs within the `renamer.py` script.

        ├── Desktop
        │   ├── rename
        │   │   ├── done      

2. Add `renamer.py` and your image files to be renamed into the `/Desktop/rename` folder. If you do not have a `done` subfolder, one will be created automatically during processing. 

3. Add file names to a spreadsheet with column A containing only the original file names and column B similarly containing the new file names. The length of each column must match; do not include column titles; example sheet setup below. 

<p align="center">
  <img src="https://github.com/elliswmartin/renamer/blob/main/csv_example.png" />
</p>

4. Save/download spreadsheet as `rename.csv` and place in `rename` folder. 

5. Open Terminal and run `renamer.py`. Images will appear in the `~/Desktop/rename/done` folder when finished.
      
        $ python3 /Users/YOUR_USERNAME/Desktop/rename/renamer.py 
          

## Background
I developed this script to handle bulk image file renaming while at Letterform Archive in San Francisco, CA. 
