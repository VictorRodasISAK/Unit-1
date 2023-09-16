"""text = str(input())
abc = "abcdefghijklmnopqrstuvwxyz"
total = 0
for let in text.lower():
    position = abc.find(let) + 1
    total += position

print(total)"""

def sum_ascii(text:str) -> int:
    total = 0
    for let in text:
        total += int(ord(let))
    return total

x = sum_ascii(text="MAth")
print(x)
