import types

def draw_stars(arr):
    for index, item in enumerate(arr):
        if isinstance (arr[index],types.IntType):
            y = arr[index]
            t = ""
            for count in range(0, y):
                t = t + "*"
                count = count - 1
            print t
        else:
            y = len(arr[index])
            t = ""
            for count in range(0,y):
                t = t + arr[index][0].lower()
            print t
draw_stars([2,3,4,5,6,7,8,"James"])
