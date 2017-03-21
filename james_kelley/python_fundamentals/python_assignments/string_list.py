str = "If monkeys like bananas, then I must be monkey!"
print str.find("monkey")

#position 3


str = "If monkeys like bananas, then I must be monkey!"
print str.replace("monkey", "alligator")

#If alligators like bananas, then I must be a alligator!


#print min and max values
x = [2,54,-2,7,12,98]
print min(x)
print max(x)


#first and last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1]


#new list
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
first_list = x[0:len(x)/2]
second_list = x[len(x)/2:len(x) - 1]
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print 'combined_list', second_list