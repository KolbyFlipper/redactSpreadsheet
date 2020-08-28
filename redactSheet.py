import tkinter, tkinter.filedialog
import os
import csv
import time


def get_new_directory_path():
	print("Select input directory path first, output directory second")
	return tkinter.filedialog.askdirectory()


def redactionSetup(headerRow, redactWords):
	print(headerRow)
	print("\n\n")
	print(redactWords)
	print("\n\n")
	hasPHI = [0] * len(headerRow)
	for i in range(len(headerRow)):
		for phrase in redactWords:
			if(phrase in headerRow[i]):
				hasPHI[i] = 1
	return hasPHI


input_directory = get_new_directory_path()
output_directory = get_new_directory_path()
files = os.listdir(input_directory)
length = len(files)

userInput = ""
inputList = []
while True:
	if(userInput.lower() == "done"):
		break
	userInput = input("Input words to be redacted(case sensitive); input one word at a time, then press enter. \nAny column with a header containing that word will be redacted from the output sheet.\nType \"done\" to move on\n")
	userInput = userInput.strip()
	if(userInput.lower() != "done"):
		inputList.append(userInput)
	print(inputList)

for i in range(length):
	file = os.path.join(input_directory,files[i]).replace("\\","/")
	fileDone = os.path.join(output_directory,files[i]).replace("\\","/")

	with open(file, 'r') as csvfile, open(fileDone, 'w', newline = '') as writeFile:
		reader = csv.reader(csvfile)
		writer = csv.writer(writeFile)
		FirstRow = True #to prevent overwriting headers
		for row in reader:
			if(FirstRow):
				#print(row)
				hasPHI = redactionSetup(row, inputList)
				FirstRow = False
				writer.writerow(row)
				continue
			track = 0
			writerRow = ["Redacted PHI"] * len(row)
			for L in row:
				if(hasPHI[track] == 0 or FirstRow):
					writerRow[track] = L
				track += 1
			writer.writerow(writerRow)

		csvfile.close()
		writeFile.close()
#, fieldnames = ["OrigAppTransactionID"]
