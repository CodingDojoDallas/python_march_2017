#Part I:
def draw_stars(arr):
	for x in arr:
		print "*" * x

numbers = [4,6,1,3,5,7,25]
draw_stars(numbers)

#Part II:

numbers = [4,6,1,3,5,7,25]
draw_stars(numbers)

def stars2(arr):
    for x in arr:
        if isinstance(x, int):
            print "*" * x
        elif isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print letter * length

x = [27, "Steven", 23, "Kim", 6, 7, "Alyson Lauren", 4, "Samantha Rae", 1, "Jessie Bronwen"]
stars2(x)
