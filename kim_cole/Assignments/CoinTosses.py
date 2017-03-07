import random

def tosses():
	print "Starting the program"
	trial = 1
	head_count = 0
	tail_count = 0
	output = ""
	output_string_complete = ""

	for i in range (0,5000):
		randomToss = random.randint(0,1)
		if randomToss == 1:
			head_count += 1
			output = "head"
			print "Attempt #", trial, ": Throwing a coin... It's a ", output, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
		else:
			tail_count += 1
			output = "tail"
			print "Attempt #", trial, ": Throwing a coin... It's a ", output, "! Got ", head_count, "head(s) so far and", tail_count, "tail(s) so far"
		trial += 1
tosses()