import random

# Function that simulates tossing a coin a number of times, counting the heads/tails
def coin_toss(reps):
    print "Starting the program..."
    head_count = 0
    tail_count = 0
    for count in range(reps):
        odds = random.randrange(1, 3)       # Random number that's either 1 or 2
        if odds == 1:
            coin = "head"
            head_count += 1
        else:
            coin = "tail"
            tail_count += 1
        print "Attempt #{}: Throwing a coin... It's a {}! ... Got {} heads(s) so far and {} tails(s) so far".format(count+1, coin, head_count, tail_count)
    print "Ending the program, thank you!"

coin_toss(5000)
