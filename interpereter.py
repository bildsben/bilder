# one day, when i can be bothered to make this shit more
# efficient, i will.

# for now, im just trying to get it to work so if you 
# are gonna complain about how inefficient it is you
# can go sym

class Builder:
	def throwerror(self, errortype, line):
		print("The builders couldn't construct your sh*tty code.")

		if errortype == "noend": errormsg = "Your code does not contain a line end. Line ends are a simple 'end' at the end of the line."
		if errortype == "notnumber": errormsg = "Your 'remember' statement does not contain a number after the first declaration of memory."
		if errortype == "falserecieved": errormsg = "You have not declared anything to remember."
		if errortype == "notnumberinp": errormsg = "You did not type a number into the input."

		if line != False:
			print("Error found on the following line: "+str(line))
		exit(errormsg)

	def ask(self, codel):
		command = codel.split(" ")

		if "end" not in command:
			self.throwerror("noend", codel)

		command.remove("end")
		command.remove("ask")
		commandcompiled = ""
		for item in command:
			commandcompiled = commandcompiled + item+ " " 

		inp = input(commandcompiled)
		try:
			inp = int(inp)
		except Exception:
			self.throwerror("notnumberinp", False)

		inpmod = "remember " + str(inp) + " end"

		self.remember(inpmod)

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

	def remember(self, codel):
		global memory

		command = str(codel).split(" ")

		if "end" not in command:
			self.throwerror("noend", codel)

		memory = command[1]

		try:
			memory = int(memory)
		except Exception as e:
			self.throwerror("notnumber", codel)
			return False

		return memory

	def think(self, codel, memory):
		command = codel.split(" ")

		if "end" not in command:
			self.throwerror("noend", codel)
			
		if memory == False:
			self.throwerror("falserecieved", codel)
		else:
			print(memory)


class Slacker:	
	def throwerror(self, errortype, line):
		print("The builders couldn't construct your sh*tty code.")

		if errortype == "notnumber": errormsg = "Your 'remember' statement does not contain a number after the first declaration of memory."
		if errortype == "falserecieved": errormsg = "You have not declared anything to remember."
		if errortype == "notnumberinp": errormsg = "You did not type a number into the input."

		if line != False:
			print("Error found on the following line: "+ str(line))
		exit(errormsg)

	def speak(self, codel):
		command = codel.split(" ")

		for item in command:
			if item == "speak":
				command.remove(item)

		itemcomp = ""

		for item in command:
			itemcomp = itemcomp + item + " "

		print(itemcomp)

	def ask(self, codel):
		command = codel.split(" ")

		command.remove("ask")
		commandcompiled = ""
		for item in command:
			commandcompiled = commandcompiled + item+ " " 

		inp = input(commandcompiled)
		try:
			inp = int(inp)
		except Exception:
			self.throwerror("notnumberinp", False)

		inpmod = "remember " + str(inp) + " end"

		self.remember(inpmod)


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

	def remember(self, codel):
		global memory

		command = str(codel).split(" ")

		memory = command[1]

		try:
			memory = int(memory)
		except Exception as e:
			self.throwerror("notnumber", codel)
			return 1

		return memory
		
	def think(self, codel, memory):
		if memory == False:
			self.throwerror("falserecieved", codel)
		else:
			print(memory)


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
memory = False

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
		elif line.split(" ")[0] == "remember":
			memory = builder.remember(line)
		elif line.split(" ")[0] == "think":
			builder.think(line, memory)
		elif line.split(" ")[0] == "ask":
			builder.ask(line)
		elif line.split(" ")[0] == "//":
			pass # // is the comment tag
		elif line.split(" ") == [""]: 
			pass #if nothing is in the line / is empty line
		else:
			if line.split(" ")[0] != "worker" and line.split(" ")[1] != "is":
				exit("\n-----ERROR-----\nUnrecognsied command:\n"+line)


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
		elif line.split(" ")[0] == "remember":
			memory = slacker.remember(line)
		elif line.split(" ")[0] == "think":
			slacker.think(line, memory)
		elif line.split(" ")[0] == "ask":
			slacker.ask(line)
		elif line.split(" ")[0] == "//":
			pass # // is the comment tag
		elif line.split(" ") == [""]: 
			pass #if nothing is in the line / is empty line
		else:
			if line.split(" ")[0] != "worker" and line.split(" ")[1] != "is":
				exit("\n-----ERROR-----\nUnrecognsied command:\n"+line)