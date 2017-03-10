import random

def scores():
    print "Scores and Grades"
    for i in range(0,10):
        random_num = random.randint(60,100)
        if (random_num < 70):
            grade="D"
        elif (random_num < 80):
            grade="C"
        elif (random_num < 90):
            grade="B"
        else:
            grade="A"
        print "Score: {}; Your grade is {}".format(random_num, grade)
    print "End of the program. Bye!"

scores()
