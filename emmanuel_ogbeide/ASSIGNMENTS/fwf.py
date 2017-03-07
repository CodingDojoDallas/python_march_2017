def odd_even():
    for count in range (1, 2001):
        if count % 2 == 0:
            print "Number is " + str(count) + ". This is an even number."
        else:
            print "Number is " + str(count) + ". This is an odd number."
odd_even()

#Above block checks for oddity of functions

def multiply(a, n):
    for index, item in enumerate(a):
        a[index] *= n
    return a
x = multiply([2,3,4,5,6,7,8], 2)
print x

#Above block multiplies list items by a value

def Blist(a):
    layered_arr = []
    for index, item in enumerate(a):
        y = a[index]
        t = []
        for count in range(0, y):
            t.append(1)
            count = count - 1
        layered_arr.append(t)
    return layered_arr
y = Blist(multiply([2,3,4,5,6,7,8], 2))
print y

#Above block does stuff I can't explain
