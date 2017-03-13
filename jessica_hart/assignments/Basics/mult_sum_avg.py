# Prints all the odd numbers from 1 to 1000
odd_num = ""                        # String made to reduce new lines
for i in range (1, 1000, 2):
    odd_num += str(i)+" "
print odd_num

# Prints all the multiples of 5 from 5 to 1,000,000
five_mult = ""                      # String made to reduce new lines
for i in range (5, 1000001, 5):     # Add 1 to reach 1,000,000
    five_mult += str(i)+" "
print five_mult

# Prints the sum of all the values in the list
a = [1, 2, 5, 10, 255, 3]
# sum = 0                           # Alternative long hand
# for i in range (0, len(a)):
#     sum += a[i]
print sum(a)

# Prints the average of the values in the list
print sum(a) / len(a)
