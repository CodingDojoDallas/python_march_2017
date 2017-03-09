str = "If monkeys like bananas, then I must be a monkey!"
print str.find('monkey')
print str.replace('monkey', 'alligator')
x = [2,3,4,5,4,5,6,4,2,3,4,5,6,4,3,5,6,6,4,4,3,8,9,87,65,4]
print x
print min(x)
print max(x)
y = ["hello",2,54,-2,7,12,98,"world"]
print y
print y[0], y[(len(y))-1]
z = [19,2,54,-2,7,12,98,32,10,-3,6]
print z
z.sort()
print z
t = z[0:(len(z))/2]
z[1:(len(z))/2] = []
z[0] = t
print z