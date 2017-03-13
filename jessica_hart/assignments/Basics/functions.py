# Function counts from 1 to 2000
def odd_even():
    for count in range(1, 2001):
        type = ""
        if count % 2 == 0:
            type = "even"
        else:
            type = "odd"
        print "Number is {}. This is an {} number.".format(count, type)

odd_even()

# Function returns a list where each value has been multiplied by 5
def multiply(arr, mult):
    new_arr = arr
    for i in range(len(new_arr)):
        new_arr[i] *= mult
    return new_arr

a = [2,4,10,16]
b = multiply(a, 5)
print b

# Function returns the multiplied list as a two-dimensional list
# Each internal list contains the number of 1's as the number in the original list
def layered_multiples(arr):
    new_arr = []
    for i in range(len(arr)):
        one_arr = []                # List to hold 1's
        for j in range(arr[i]):
            one_arr.append(1)       # Appends 1's to a list determined by the number in original list
        new_arr.append(one_arr)     # Append the 1's list each iteration
    return new_arr

x = layered_multiples(multiply([2,4,5],3))
print x
