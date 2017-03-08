import random

def cointosses():
    count1 = 0
    count2 = 0
    for i in range(1,5001):
        rando = random.randint(1,2)
        if rando == 1:
            count1 = count1 + 1
            print "Attempt #" + str(i) + ": Throwing a coin...  It's a head! ... Got " + str(count1) + " head(s) so far"
        else:
            count2 = count2 + 1
            print "Attempt #" + str(i) + ": Throwing a coin...  It's a tail! ... Got " + str(count2) + " tail(s) so far"
cointosses()
