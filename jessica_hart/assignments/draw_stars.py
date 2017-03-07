# from numbers import Number
# def draw_stars(lst):
#     for i in range(len(lst)):
#         string = ""
#         if isinstance(lst[i], Number):      # Check if the list index contains a number
#             char = "*"
#             for j in range(lst[i]):
#                 string += char
#         else:
#             char = lst[i][0].lower()        # Assume there is a string if no number
#             for j in range(len(lst[i])):
#                 string += char
#         print string


# Function takes a list of numbers and prints out *, non-numbers display the first letter instead
def draw_stars_pythonic(lst):
    for i in lst:
        if isinstance(i, int):      # Check if the list index contains a number
            print "*" * i
        elif isinstance(i, str):
            char = i[0].lower()     # Check if it's a letter instead and print the first character
            print char * len(i)

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars_pythonic(x)
