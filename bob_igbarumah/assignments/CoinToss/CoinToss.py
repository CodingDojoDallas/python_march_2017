import random

def toss():
    head = 1
    tail = 0
    countH = 0
    countT = 0

    for i in range(1,5001):
        x = random.random()
        x_round = round(x)
        if x_round == head:
           countH+=1
           print 'Attempt', '#'+str(i)+':',' Throwing a coin...','Its a head!','...','Got ',countH,'head(s)','so far and',countT,'tails so far'
        else:
           countT+=1
           print 'Attempt', '#'+str(i)+':',' Throwing a coin...','Its a tail!','...','Got ',countH,'head(s)','so far and',countT,'tails so far'

toss()
