import random

def scores():
	print "Scores and Grades"
	for i in range (0,10):
		randomScore = random.randint(60,100)
		if randomScore > 89:
			grade = "A"
		elif randomScore > 79:
			grade = "B"
		elif randomScore > 69:
			grade = "C"
		else:
			grade = "D"
		print "Score: {}; Your grade is {}".format(randomScore,grade)
	print "End of this Grade Report.  BYE!"
scores()