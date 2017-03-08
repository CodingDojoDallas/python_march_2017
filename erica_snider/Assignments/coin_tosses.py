import random

def tosses():
    print "Starting the program..."
    tails = 0
    heads = 0
    for i in range(0,5000):
        toss = round(random.random())
        if (toss == 0): # 0 is tails
            result = "tail"
            tails += 1
        elif (toss == 1): # 1 is heads
            result = "head"
            heads += 1
        else:
            print "unexpected value for toss"
        print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} head(s) so far and {} tail(s) so far".format(heads+tails,result,heads,tails)
    print "Ending program. Thank you!"

tosses()
