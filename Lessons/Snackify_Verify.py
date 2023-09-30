"""# Things that I learned in Snackify

#Bishop movement to verify if its possible
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs(a - c) == abs(b - d):
    print("YES")
else:
    print("NO")

#Verify if is the same color in the chessboard (BLACK)
column = int(input())
row = int(input())

if row % 2 == column % 2:
    print('BLACK')
else:
    print('WHITE')

#Verify iif is the same color in the chessboard
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 + y1 + x2 + y2) % 2 == 0:
    print('YES')
else:
    print('NO')

#King move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print('YES')
else:
    print('NO')

#Knight move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')

#To get the unit and the ten separately (2 numbers)
a = int(input())
print(a // 10, a % 10)

#Print last 2 digits
print(int(input()) % 100)

#Print just the ten
x = int(input())
print(x // 10 % 10)

#Print just hundred
x = int(input())
print(x // 100)"""