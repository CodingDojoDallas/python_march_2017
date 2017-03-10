#Multiples
   #part 1
for count in range(1,1001):
     if count % 2 != 0:
         print count


    #part 2
for count in range(5,1000001):
    if count % 5 == 0:
       print count

#Sum List
sum = 0
a =[1,2,5,10,255,3]
for count in a:
    sum+=count
print sum

#Average
a =[1,2,5,10,255,3]
num = len(a)
sum = 0
a =[1,2,5,10,255,3]
for count in a:
    sum+=count
print sum/num
