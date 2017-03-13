import types
#PART 1
def draw_stars(x):

    for i in x:
        print "\n"
        for j in range(0,i):

                print "*",




x = [4,6,2,1]
print
draw_stars(x)

#part 2
def draw_star(a):

    for i in x:
        print "\n"
        y = i
        if isinstance(i,types.StringType):
                y = len(i)

                p = i.lower()
        for j in range(0,y):
            if  isinstance(i,types.IntType):

                 print "*",
            else:

                 print p[0],
x = [4,"Tom",1,"Michael",5,7,"Jimmy Smith"]
#print
draw_star(x)
