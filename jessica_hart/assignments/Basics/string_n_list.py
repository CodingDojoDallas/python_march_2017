# Print the position of the first instance of the word "monkey"
# Then create a new string where the word "monkey" is replaced with the word "alligator"
str = "If monkeys like bananas, then I must be a monkey!"
print "Index of the first monkey:", str.find("monkey")
new_str = str.replace("monkey", "alligator", 1)
print new_str

# Print the min and max values in a list
x = [2,54,-2,7,12,98]
print "The min and max are {} and {} respectively".format(min(x), max(x))

# Print the first and last values in a list
# Create a new list containing only the first and last values in the original
x = ["hello",2,54,-2,7,12,98,"world"]
print "The first and last values are {} and {}".format(x[0], x[-1])   # Alternatives: len(x)-1
y = [x[0], x[-1]]
print y

# Start with a list. Sort your list first. Then, split your list in half.
# Push the list created from the first half to position 0 of the list created from the second half
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()            # Sort the list in ascending order
print x
x1 = x[:len(x)/2]   # Split the list into two halves
x2 = x[len(x)/2:]
print x1, x2
x2.insert(0, x1)    # Insert the first list into index 0 of the second list
print x2
