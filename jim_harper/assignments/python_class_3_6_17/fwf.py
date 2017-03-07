#Fun with Functions

'''
def odd_even():
    a = 1
    while a <= 2000:
        a = int(a)
        if (a % 2) != 0:
            print "Number is {}. This is an odd number.".format(a)
            a+=1

        else:
            print "Number is {}. This is an even number".format(a)
            a+=1

odd_even()'''

def multiply():
    a = [2,4,10,16]
    i = 0
    x = 0
    b = []

    while i < len(a):
        x = a[i]*5
        b.append(x)
        i+=1

    print b

multiply()
