str = "If monkeys like bananas, then I must be a monkey!"
print str.find("monkey")
new_str = str.replace("monkey","alligator")
print new_str

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0] # first
print x[len(x)-1] # last
y = [x[0], x[len(x)-1]]
print y

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x.sort()
begin = x[:len(x)/2]
end = x[len(x)/2:]
end.insert(0,begin)
print end
