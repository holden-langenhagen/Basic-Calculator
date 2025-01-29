def add(arg1, arg2):
    return float(arg1) + float(arg2)


def sub(arg1, arg2):
    return float(arg1) - float(arg2)


def mult(arg1, arg2):
    return float(arg1) * float(arg2)


def div(arg1, arg2):
    return float(arg1) / float(arg2)


import re

# Taking input from the user and formatting it into list
# Example input: 5-5*6/12+13-2*6
s = input("Input your expression to be calculated (+,-,*,/): \n->")
l = re.split(r'([\d]+)', s)[1:-1]

# Loop through characters to isolate higher order ops (*,/)
i = 0
while i in range(len(l) - 2):
    if l[i + 1] == "*":
        l[i] = mult(l[i], l[i + 2])
        if len(l) == 1: break
    elif l[i + 1] == "/":
        l[i] = div(l[i], l[i + 2])
        if len(l) == 1: break
    else:
        # Skip over lower order ops (+,-)
        i += 2
        continue
    # Condense solved term
    del l[i + 1:i + 3]

# Loop through remaining characters to calculate lower ops (+,-)
i = 0
while i in range(len(l) - 2):
    if l[i + 1] == "+":
        l[i] = add(l[i], l[i + 2])
        if len(l) == 1: break
    elif l[i + 1] == "-":
        l[i] = sub(l[i], l[i + 2])
        if len(l) == 1: break
    else:
        # Throw error if unexpected character given as input
        print("input not valid, please use +,-,*,/ operators only")
        exit()
    # Condense solved term
    del l[i + 1:i + 3]

print(l[0])
