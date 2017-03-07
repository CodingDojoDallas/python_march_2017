import random

def scores():
    print 'Scores and Grades'
    for i in range(0,10):
        num = random.randint(60,100)

        if num > 89:
            grade = 'A'

        elif num > 79:
            grade = 'B'

        elif num > 69:
            grade = 'C'

        else:
            grade = 'D'

        print "Score: {}; Your grade is {}".format(num,grade)

    print "End of the program. Bye!"

scores()
