class Builder:
	def throwerror(self, errortype, line):
		print("The builders couldn't construct your sh*tty code.")

		if errortype == "noend": errormsg = "Your code does not contain a line end. Line ends are a simple 'end' at the end of the line."
		print("Error found on the following line: "+line)
		exit(errormsg)

	def speak(self, codel):
		command = codel.split(" ")

		if "end" not in command:
			self.throwerror("noend", codel)
		
		for item in command:
			if item == "speak":
				command.remove(item)
			if item == "end":
				command.remove(item)

		itemcomp = ""

		for item in command:
			itemcomp = itemcomp + item + " "

		print(itemcomp)


	def yell(self, codel):
		command = codel.split(" ")


		if "end" not in command:
			self.throwerror("noend", codel)
		
		for item in command:
			if item == "yell":
				command.remove(item)
			if item == "end":
				command.remove(item)

		itemcomp = ""

		for item in command:
			itemcomp = itemcomp + item + " "

		itemcomp = itemcomp.upper()
		print(itemcomp)

	def whisper(self, codel):
		command = codel.split(" ")


		if "end" not in command:
			self.throwerror("noend", codel)
		
		for item in command:
			if item == "whisper":
				command.remove(item)
			if item == "end":
				command.remove(item)

		itemcomp = ""

		for item in command:
			itemcomp = itemcomp + item + " "

		itemcomp = itemcomp.lower()

		print(itemcomp)

class Slacker:
	def speak(self, codel):
		command = codel.split(" ")

		for item in command:
			if item == "speak":
				command.remove(item)

		itemcomp = ""

		for item in command:
			itemcomp = itemcomp + item + " "

		print(itemcomp)


	def yell(self, codel):
		command = codel.split(" ")
		
		for item in command:
			if item == "yell":
				command.remove(item)

		itemcomp = ""

		for item in command:
			itemcomp = itemcomp + item + " "

		itemcomp = itemcomp.upper()
		print(itemcomp)

	def whisper(self, codel):
		command = codel.split(" ")
		
		for item in command:
			if item == "whisper":
				command.remove(item)

		itemcomp = ""

		for item in command:
			itemcomp = itemcomp + item + " "

		itemcomp = itemcomp.lower()

		print(itemcomp)


# Breakdown of "bilder":
# Files end in .bild
# More info to come

import sys

builder = Builder()
slacker = Slacker()

args = []

for item in sys.argv:
	if item == "interpereter.py":
		pass
	else:
		args.append(item)

if len(args) > 1:
	exit("Too many arguments.")

file = open(sys.argv[1], "r")
code = file.read()
file.close()

usingBuilder = False
usingSlacker = False

for line in code.split("\n"):
	if line == "worker is slacker":
		usingSlacker = True
		usingBuilder = False
	elif line == "worker is builder":
		usingBuilder = True
		usingSlacker = False

	if usingBuilder == False and usingSlacker == False:
		exit("\n-----ERROR-----\nNo worker defined.\nUse the following format to set worker type.\nworker is builder\nworker is slacker")

	if usingBuilder:
		if line == "worker is slacker":
			usingSlacker = True
			usingBuilder = False
		elif line.split(" ")[0] == "speak":
			builder.speak(line)
		elif line.split(" ")[0] == "yell":
			builder.yell(line)
		elif line.split(" ")[0] == "whisper":
			builder.whisper(line)
		elif line.split(" ")[0] == "//":
			pass # // is the comment tag
		elif line.split(" ") == [""]: 
			pass #if nothing is in the line / is empty line
		else:
			if line.split(" ")[0] != "worker" and line.split(" ")[1] != "is":
				exit("\n-----ERROR-----\nUnrecognsied command BUILDER:\n"+line)


	elif usingSlacker:
		if line == "worker is builder":
			usingBuilder = True
			usingSlacker = False
		elif line.split(" ")[0] == "speak":
			slacker.speak(line)
		elif line.split(" ")[0] == "yell":
			slacker.yell(line)
		elif line.split(" ")[0] == "whisper":
			slacker.whisper(line)
		elif line.split(" ")[0] == "//":
			pass # // is the comment tag
		elif line.split(" ") == [""]: 
			pass #if nothing is in the line / is empty line
		else:
			if line.split(" ")[0] != "worker" and line.split(" ")[1] != "is":
				exit("\n-----ERROR-----\nUnrecognsied command BUILDER:\n"+line)