for each in range(1,100): # used 100 rather than 1000 to shorten output
    if (each%2 == 1):
        # print each
        pass


for each in range(5,1001): # used 1001 rather than 1000000 to shorten output
    if (each%5 == 0):
        # print each
        pass

a = [1, 2, 5, 10, 255, 3]
total = 0
for each in a:
    total += each
print total

a = [1, 2, 5, 10, 255, 3]
total = 0
count = 0
for each in a:
    total += each
    count += 1
print total/count
