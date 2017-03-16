import random

# Functions prints a specified number of random grades
def scores_grades(reps):
    print "Scores and Grades"
    for i in range(reps):
        score = random.randrange(60, 101)   # Random number between 60 and 100
        if score > 89:
            grade = "A"
        elif score > 79 and score < 90:
            grade = "B"
        elif score > 69 and score < 80:
            grade = "C"
        else:
            grade = "D"
        print "Score: {}; Your grade is {}".format(score, grade)
    print "End of the program. Bye!"

scores_grades(10)
