def odd_or_even():
    for count in range(1, 201):  # used end condition 201 rather than 2001 to shorten output
        if (count%2==0):
            odd_or_even = "even"
        else:
            odd_or_even = "odd"
        print "Number is {}. This is an {} number.".format(count, odd_or_even)

# odd_or_even()


def multiply(given_list,n):
    index = 0
    for item in given_list:
        given_list[index] = item * n
        index += 1
    return given_list

# a = [2,4,10,16]
# b = multiply(a,5)
# print b


def layered_multiples(arr):
    # your code here
    new_array = []
    for i in range(0,len(arr)): # for each value in the given array
        temp_array = []
        for k in range(0,arr[i]): # list the proper amount of 1's
            temp_array.append(1)
        new_array.insert(i,temp_array)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
