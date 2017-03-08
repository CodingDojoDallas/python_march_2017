import random

def scores():
    print 'Scores and Grades'
    for value in range(0,10):
        rando = random.randint(60,100)
        if rando > 89:
            print "Score: " + str(rando) + "; Your grade is A"
        elif rando > 79:
            print "Score: " + str(rando) + "; Your grade is B"
        elif rando > 69:
            print "Score: " + str(rando) + "; Your grade is C"
        else:
            print "Score: " + str(rando) + "; Your grade is D"
    print "End of The Program. Bye!"
scores()
