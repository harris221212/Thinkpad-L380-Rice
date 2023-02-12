import sys
import re
import subprocess
import os

# ctrl+f IMPROVE to find things I want to improve

if not len(sys.argv) == 3:
	print("Error, incorrect number of arguments. Correct format is (groffdoc input output)")
	exit()

if not os.path.isfile(sys.argv[1]):
	print("Error, file doesn't exist")
	exit()

f = open(sys.argv[1], "r")
tempFileNameArray = sys.argv[2].split(".")
tempFileName = tempFileNameArray[0]
groff = open(tempFileName, "w")
fileString = f.read()
f.close()

splitString = fileString.split("\n")

# groff file setup
groff.write(".nr HM 1\n")
curLine = 0
insideCode = False

# function to do checking for syntax
def code(curLine):
	curLine += 1
	codeString = ""
	while not splitString[curLine] == "```":
		codeString += splitString[curLine] + "\n"
		curLine += 1
	codeString = codeString.rstrip() # strip trailing newline
	fileName = "temp." + language # IMPROVE
	f = open(fileName, "w")
	f.write(codeString)
	f.close()
	#result = subprocess.Popen(["highlight", "-O", "truecolor", fileName, "|", "groffhl"], stdout=subprocess.PIPE)
	ps = subprocess.run(["highlight", "-O", "truecolor", fileName], check=True, capture_output=True) # get highlighted code
	processNames = subprocess.run(["groffhl"], input=ps.stdout, capture_output=True) # convert to groff format with groffhl
	codeFormatted = processNames.stdout.decode('utf-8').strip() # get result as string
	codeFormatted = codeFormatted.replace("]\n", "]\n.br\n") # add line breaks in the code part to make it format properly
	# following code is to replace default highlight colours with my preffered colours
	codeFormatted = codeFormatted.replace("1.000000f", "0.169000f") # replace white with black
	codeFormatted = codeFormatted.replace("0.815686f 0.815686f 0.270588f", "0.000000f 0.000000f 1.000000f") # replace color of import
	codeFormatted = codeFormatted.replace("0.325490f 0.741176f 0.988235f", "0.000000f 0.502000f 0.000000f") # comments
	codeFormatted = codeFormatted.replace("0.058824f 0.576471f 0.058824f", "0.149000f 0.498000f 0.600000f") # name = value
	codeFormatted = codeFormatted.replace("0.411765f 0.780392f 0.537255f", "1.000000f 0.000000f 0.000000f") # null
	codeFormatted = codeFormatted.replace("0.901961f 0.298039f 0.901961f", "0.035000f 0.525000f 0.345000f") # numbers
	codeFormatted = codeFormatted.replace("0.776471f 0.254902f 0.776471f", "0.639000f 0.082000f 0.082000f") # string
	codeFormatted = codeFormatted.replace("0.972549f 0.819608f 0.819608f", "1.000000f 0.000000f 0.000000f") # newline
	groff.write(codeFormatted + "\n") # write to file


def paragraph(text):
	# bold and italic
	text = text.replace(".", "\[char46]")
	
	pattern = re.compile(r"(\*\*\*([^**]|.|[^**]*)\*\*\*)")
	match = pattern.findall(text)
	for pair in match:
		newString = "\n" + ".BI \"" + pair[1] + "\"\c\n"
		text = text.replace(pair[0], newString)
		
	# bold
	pattern = re.compile(r"(\*\*([^**]|.|[^**]*)\*\*)")
	match = pattern.findall(text)
	for pair in match:
		newString = "\n" + ".B \"" + pair[1] + "\"\c\n"
		text = text.replace(pair[0], newString)
	
	# italic
	pattern = re.compile(r"(\*([^*]|.|[^*]*)\*)")
	match = pattern.findall(text)
	for pair in match:
		newString = "\n" + ".I \"" + pair[1] + "\"\c\n"
		text = text.replace(pair[0], newString)
		
	# monospace
	pattern = re.compile(r"(`([^`]|.|[^`]*)`)")
	match = pattern.findall(text)
	for pair in match:
		newString = "\n" + ".CW \"" + pair[1] + "\"\c\n"
		text = text.replace(pair[0], newString)
	
	
	
	#text = text.replace("\n ", "\n")
	groff.write(text)



def check(x, curLine):
	global insideCode
	global language
	# check if line is a title
	if x[0] == "#":
		groff.write(".TL\n")
		groff.write(x[2:len(x)] + "\n")
		groff.write(".PP\n")
		
	# check for code blocks
	elif x[0:3] == "```":
		if insideCode:
			insideCode = False
		else:
			language = x[4:len(x)]
			language = language.lower()
			if language == "python":
				language = "py"
			if language == "haskell":
				language = "has"
			if language == "c++":
				language = "cpp"
			code(curLine)
			insideCode = True
	
	elif not insideCode:
		paragraph(x)


for x in splitString:
	if not len(x) == 0:
		check(x, curLine)
	curLine += 1
		


groff.close()
pdfFileName = sys.argv[2]
pdfOutput = subprocess.run(["groff", "-ms", "-Tpdf", tempFileName], capture_output=True) # get highlighted code
pdf = pdfOutput.stdout
pdfFile = open(pdfFileName, "wb")
pdfFile.write(pdf)
pdfFile.close()




# Spare shit: 

