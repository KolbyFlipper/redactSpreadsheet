# redactSpreadsheet
An easy to use python tool to batch redact spreadsheets in a folder. Simply input your key words, and if the header of a column contains any of those key words, the column will be redacted.

Dependencies: Tkinter, Python 3.8.5+. 

Work flow: 
Run py redactSheet.py
Select the directory where your spreadsheets are stored- these will not be edited.
Select the directory where you would like the redacted spreadsheets to go
Input your key words, 1 per line. 

The selected output folder will contain your redacted spreadsheets. 

Tkinter is used to open file dialogues, if you are using this script in an environment where it cannot be installed, you can replace that line by hardcoding the file directories in place of the variables where the get_new_directory_path(): function is called.
