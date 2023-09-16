# Given 2 numbers, A and B, Output TRUE if one of them is 20 or if their sum is 20.
x = int(input())
y = int(input())
add = x + y
if x == 20 or y == 20:
    output = True
else:
    if add == 20:
        output = True
    else:
        output = False
print(output)

# HL Part
a = [5, 9, 10, 11]
b = [5, 15, 5, 17]
c = 20
if c in a or c in b:
    output = True
else:
    if sum(a) == c or sum(b) == c:
        output = True
    else:
        output = False
print(output)

