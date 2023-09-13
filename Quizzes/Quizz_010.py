month = str(input())
print(month.center(32))
print(f"Su   Mo   Tu   We   Th   Fr   Sa")
for x in range(1,32):
    print(str(x).center(2), end="   ")
    if x % 7 == 0:
        print("\n")

"""print("\n")
def month(m:str):
    months_31 = ["January", "March", "May", "July", "August", "October", "December"]
    if m in months_31:
        print(m.center(32))
        print(f"Su   Mo   Tu   We   Th   Fr   Sa")
        for n in range(1,32):
            print(str(n).center(2), end="   ")
            if n % 7 == 0:
                print("\n")
    return m

month(m="January")"""