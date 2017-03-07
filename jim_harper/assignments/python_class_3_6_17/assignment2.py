str = 'If monkeys like bananas, then I must be a monkey!'

print str.replace('monkey','alligator',1)

x = [2,54,-2,7,12,98]
print max(x)
print min(x)

x = ['hello',2,54,-2,7,12,98,'world']
print x[:1] + x[7:]


y = [19,2,54,-2,7,12,98,32,10,-3,6]
y.sort()
z = y[:5]
y = y[5:]
y.insert(0,z)
print y
